# Copyright 2015 Canonical, Ltd.
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

""" Palette Loader """


def _get_hex(color, palette):
    if not color:
        return ""
    return palette[color]


def load_palette(palette_conf):
    """ Load style from configuration, see ubuntui.conf

    Arguments:
    palette_conf: Toml configuration containing a `style` table
    """
    palette_map = []
    for k, v in palette_conf['style'].items():
        color1, color2, color3, color4, color5 = v
        palette_map.append((k,
                            _get_hex(color1),
                            _get_hex(color2),
                            _get_hex(color3),
                            _get_hex(color4),
                            _get_hex(color5)))
    return palette_map
