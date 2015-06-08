# Copyright 2015 Canonical, Ltd.

""" Base Frame Widget """

from urwid import Frame as _Frame
from urwid import WidgetWrap, AttrWrap, Pile, Text


class Header(WidgetWrap):
    """ Header Widget

    This widget uses the style key `frame_header`

    :param str title: Title of Header
    :returns: Header()
    """
    def __init__(self, title):
        title = title if title else "Ubuntu"
        self.title_widget = AttrWrap(Text(title), "frame_header")
        self.pile = Pile([self.title_widget])
        super().__init__(self.pile)


class Frame(WidgetWrap):
    def __init__(self, header, body, footer):
        self.frame = _Frame(body,
                            header,
                            footer)
        super().__init__(self.frame)
