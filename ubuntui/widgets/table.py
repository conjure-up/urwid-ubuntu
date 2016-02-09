# Copyright 2014-2016 Canonical, Ltd.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals

from urwid import (Columns, Pile, Divider)
from ubuntui.utils import Color


class Table:
    def __init__(self):
        self.rows = Pile([])

    def addHeadings(self, headings):
        """ Takes list of headings and converts them to column header
        with appropriate color

        Params:
        headings: List of column text headings
        """
        cols = []
        for h in headings:
            h = Color.column_header(h)
            cols.append(h)
            cols.append(('fixed', 1,
                         Color.column_header(
                             Divider("\N{BOX DRAWINGS LIGHT VERTICAL}"))))
        self.addRow(Columns(cols))

    def addColumns(self, columns):
        cols = []
        for c in columns:
            cols.append(c)
            cols.append(('fixed', 1,
                         Divider("\N{BOX DRAWINGS LIGHT VERTICAL}")))
        self.addRow(Columns(cols))

    def addRow(self, item):
        """ Appends widget to Pile
        """
        self.rows.contents.append((item, self.rows.options()))
        self.rows.contents.append((
            Divider("\N{BOX DRAWINGS LIGHT HORIZONTAL}"),
            self.rows.options()))

    def render(self):
        return self.rows
