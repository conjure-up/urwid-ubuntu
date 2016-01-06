# Copyright (c) 2015 Canonical Ltd.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from __future__ import unicode_literals
from .widgets.input import StringEditor
from .utils import Color, Padding
from collections import OrderedDict
from urwid import (Pile, WidgetWrap, Text,
                   Button, Filler, Columns, Divider,
                   signals, emit_signal, connect_signal)

""" re-usable dialog widget """


class Dialog(WidgetWrap):

    __metaclass__ = signals.MetaSignals
    signals = ['done']
    # key_conversion_map = {'tab': 'down', 'shift tab': 'up'}

    input_items = []

    def __init__(self, title, cb):
        self.title = title
        self.cb = cb
        self.input_selection = OrderedDict()
        connect_signal(self, 'done', self.cb)
        super().__init__(self._build_widget())

    def _build_buttons(self):
        buttons = [
            Padding.line_break(""),
            Color.button_primary(
                Button("Confirm", self.submit),
                focus_map='button_primary focus'),
            Color.button_secondary(
                Button("Cancel", self.cancel),
                focus_map='button_secondary focus'),
        ]
        return Pile(buttons)

    def _build_widget(self, **kwargs):
        total_items = [
            Padding.center_60(Text(self.title, align="center")),
            Padding.center_60(
                Divider("\N{BOX DRAWINGS LIGHT HORIZONTAL}", 1, 1))
        ]
        if self.input_items:
            for item in self.input_items:
                key = item[0]
                caption = item[1]
                try:
                    mask = item[2]
                except:
                    mask = None
                self.input_selection[key] = StringEditor(caption="", mask=mask)
                col = Columns(
                    [
                        ("weight", 0.5, Text(caption, align="right")),
                        Color.string_input(self.input_selection[key],
                                           focus_map="string_input focus")
                    ]
                )
                total_items.append(Padding.center_60(col))
        total_items.append(
            Padding.center_60(
                Divider("\N{BOX DRAWINGS LIGHT HORIZONTAL}", 1, 1)))
        total_items.append(Padding.center_20(self._build_buttons()))
        return Filler(Pile(total_items), valign='middle')

    def submit(self, button):
        self.emit_done_signal(self.input_selection)

    def cancel(self, button):
        raise SystemExit("Installation cancelled.")

    def emit_done_signal(self, *args):
        emit_signal(self, 'done', *args)
