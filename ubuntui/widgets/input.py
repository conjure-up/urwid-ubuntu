""" Re-usable input widgets
"""

from urwid import (Edit,
                   IntEdit,
                   RadioButton,
                   WidgetWrap,
                   Pile,
                   Columns)
import logging
import re

log = logging.getLogger("widgets.input")
first_true = Ellipsis  # default value that is distinguishable from None


class StringEditor(WidgetWrap):
    """ Edit input class
    Initializes and Edit object and attachs its result
    to the `value` accessor.
    """

    def __init__(self, caption=None, default=None, **kwargs):
        if caption is None:
            caption = ""
        self._edit = Edit(caption=caption, **kwargs)
        if default is not None:
            self._edit.set_edit_text(default)
        self.error = None
        super().__init__(self._edit)

    def keypress(self, size, key):
        if self.error:
            self._edit.set_edit_text("")
            self.error = None
        return super().keypress(size, key)

    def set_error(self, msg):
        self.error = msg
        return self._edit.set_edit_text(msg)

    @property
    def value(self):
        if self._edit.get_edit_text() == "":
            return None
        return self._edit.get_edit_text()

    @value.setter  # NOQA
    def value(self, value):
        self._edit.set_edit_text(value)


class PasswordEditor(StringEditor):
    """ Password input prompt with masking
    """

    def __init__(self, caption=None, mask="*", **kwargs):
        super().__init__(caption, mask=mask, **kwargs)


class RealnameEditor(StringEditor):
    """ Username input prompt with input rules
    """

    def keypress(self, size, key):
        ''' restrict what chars we allow for username '''

        realname = r'[a-zA-Z0-9_\- ]'
        if re.match(realname, key) is None:
            return False

        return super().keypress(size, key)


class UsernameEditor(StringEditor):
    """ Username input prompt with input rules
    """

    def keypress(self, size, key):
        ''' restrict what chars we allow for username '''

        userlen = len(self.value)
        if userlen == 0:
            username = r'[a-z_]'
        else:
            username = r'[a-z0-9_-]'

        # don't allow non username chars
        if re.match(username, key) is None:
            return False

        return super().keypress(size, key)


class MountEditor(StringEditor):
    """ Mountpoint input prompt with input rules
    """

    def keypress(self, size, key):
        ''' restrict what chars we allow for mountpoints '''

        mountpoint = r'[a-zA-Z0-9_/\.\-]'
        if re.match(mountpoint, key) is None:
            return False

        return super().keypress(size, key)


class IntegerEditor(WidgetWrap):
    """ IntEdit input class
    """

    def __init__(self, caption=None, default=0):
        if caption is None:
            caption = ""
        self._edit = IntEdit(caption=caption, default=default)
        super().__init__(self._edit)

    @property
    def value(self):
        return self._edit.get_edit_text()


class Selector(WidgetWrap):
    """ Radio selection list of options
    """

    def __init__(self, opts, default=first_true):
        """
        :param list opts: list of options to display
        :param default: Value of option to be selected by default.  Defaults
            to the first item in the list.  If ``None``, no item will be
            selected by default.
        """
        self.opts = opts
        self.default = default
        self.group = []
        self._add_options()
        super().__init__(self._add_options())

    def _add_options(self):
        cols = []
        for item in self.opts:
            if self.default is first_true:
                state = 'first True'
            else:
                state = item == self.default
            cols.append((8, RadioButton(self.group, item, state=state)))
        return Columns(cols)

    @property
    def value(self):
        """ Returns value of selection.

        If the value is Yes/No will return True/False
        Any other values return the label.
        """
        for item in self.group:
            log.debug(item)
            if item.get_state() and item.label == "Yes":
                return True
            if item.get_state() and item.label == "No":
                return False
            if item.get_state():
                return item.label
        return None

    def set_default(self, item, state=False):
        """ Sets the default state of an item

        Arguments:
        item: name of item to change state of
        state: sets item to True or False
        """
        for i in self.group:
            if i.label == item:
                i.set_state(state)


class YesNo(Selector):
    """ Yes/No selector
    """

    def __init__(self, default=None):
        """
        :param default: Default value, if any.  Can be ``'Yes'``, ``'No'``,
            or ``None`` (which will select neither by default).  Defaults to
            ``None``.
        """
        opts = ['Yes', 'No']
        super().__init__(opts, default)


class SelectorHorizontal(Selector):
    """ This is to use rows instead of columns for selection list
    """
    def _add_options(self):
        rows = []
        for item in self.opts:
            rows.append((RadioButton(self.group, item)))
        return Pile(rows)
