# Copyright 2015 Canonical, Ltd.

""" Base Frame Widget """

from urwid import Frame as _Frame
from urwid import WidgetWrap, Pile, Text


class Header(WidgetWrap):
    """ Header Widget

    This widget uses the style key `frame_header`

    Arguments:
    title: Title text
    align: Text alignment, defaults=left
    """
    def __init__(self, title, align="left"):
        self._title = Text(("frame_header", title), align=align)
        self.pile = Pile([self.title_widget])
        super().__init__(self.pile)

    @property
    def title(self):
        return self._title.get_text()[0]

    @title.setter
    def title(self, val, attr=None):
        """
        Sets header title text

        Arguments:
        val: Text value
        attr: (optional) Attribute lookup
        """
        if attr is not None:
            self._title.set_text(val)
        else:
            self._title.set_text((attr, val))


class Frame(WidgetWrap):
    def __init__(self, header, body, footer):
        self.frame = _Frame(body,
                            header,
                            footer)
        super().__init__(self.frame)
