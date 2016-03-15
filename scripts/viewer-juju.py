#!/usr/bin/env python3

import sys
import os
import json

toplevel = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
fixtures_dir = os.path.join(toplevel, 'fixtures')
maas_data = os.path.join(fixtures_dir, 'maas_nodes.json')
juju_data = os.path.join(fixtures_dir, 'juju_status.json')
sys.path.insert(0, toplevel)

from urwid import Text  # noqa
from ubuntui.ev import EventLoop  # noqa
from ubuntui.frame import Frame  # noqa
from ubuntui.widgets.table import Table  # noqa
from ubuntui.palette import STYLES  # noqa
from ubuntui.widgets.juju.service import ServiceWidget  # noqa
from ubuntui.widgets.juju.machine import MachineWidget  # noqa
import q


class ServiceUI(Frame):
    def __init__(self, juju_state):
        table = Table()
        table.addHeadings([
            Text('Service'),
            Text('Hardware'),
            Text('Hostname'),
            Text('Machine'),
        ])
        for name, service in juju_state['Services'].items():
            s = ServiceWidget(name, service)
            q(s)
            for u in s.Units:
                m = MachineWidget(juju_state['Machines'][u.Machine.get_text()[0]])
                table.addColumns(u.Name.get_text()[0], [
                    u.Name,
                    m.Hardware,
                    m.DNSName,
                    u.Machine
                ])
        super().__init__(body=table.render())


def unhandled_input(key):
    if key in ['q', 'Q']:
        EventLoop.exit(0)


def main():
    with open(juju_data) as fp:
        juju_state = json.load(fp)
    ui = ServiceUI(juju_state)
    EventLoop.build_loop(ui, STYLES, unhandled_input=unhandled_input)
    EventLoop.run()

if __name__ == '__main__':
    main()
