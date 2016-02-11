from __future__ import unicode_literals

from urwid import (Columns, ListBox, Divider)
from ubuntui.utils import Color


class Table:
    def __init__(self):
        self._rows = []
        self._row_id = []

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
        self.addRow(Columns(cols))

    def addColumns(self, row_id, columns):
        """ Convert list of widgets to Columns and add to a table row

        Arguments:
        row_id: unique id of new row
        columns: list of columns
        """
        if row_id not in self._row_id:
            self._row_id.append(row_id)
            self.addRow(Columns(columns))

    def addRow(self, item):
        """ Appends widget to Pile
        """
        self._rows.append(item)
        self._rows.append(
            Divider("\N{BOX DRAWINGS LIGHT HORIZONTAL}"))

    def render(self):
        return ListBox(self._rows)
