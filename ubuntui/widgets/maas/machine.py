# Copyright 2015-2016 Canonical, Ltd.
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

""" Represents a Single MAAS node UI widget
"""

from urwid import WidgetWrap, Text


class MachineWidget(WidgetWrap):
    def __init__(self, machine):
        """ Init

        Params:
        machine: Maas Machine class
        """
        self.machine = machine
        _attrs = ['hostname',
                  'status',
                  'zone',
                  'cpu_count',
                  'storage',
                  'architecture',
                  'memory',
                  'power_type',
                  'power_state',
                  'system_id',
                  'ip_addresses',
                  'macaddress_set',
                  'tag_names',
                  'owner']
        for m in _attrs:
            if isinstance(m, list):
                setattr(self, m, Text(", ".join(self.machine.get(m))))
            else:
                setattr(self, m, Text(str(self.machine.get(m))))
