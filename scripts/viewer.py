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
from ubuntui.widgets.maas.machine import MachineWidget  # noqa


class MachineUI(Frame):
    def __init__(self, machine_view):
        table = Table()
        table.addHeadings([
            Text('Hostname'),
            Text('CPU'),
            Text('Storage'),
            Text('Memory'),
        ])
        for m in machine_view:
            m = MachineWidget(m)
            table.addColumns([
                m.hostname,
                m.cpu_count,
                m.storage,
                m.memory
            ])
        super().__init__(table.render())


def unhandled_input(key):
    if key in ['q', 'Q']:
        EventLoop.exit(0)


def main():
    with open(maas_data) as fp:
        maas_machines = json.load(fp)
    machine_view = maas_machines
    ui = MachineUI(machine_view)
    EventLoop.build_loop(ui, STYLES, unhandled_input=unhandled_input)
    EventLoop.run()

if __name__ == '__main__':
    main()
