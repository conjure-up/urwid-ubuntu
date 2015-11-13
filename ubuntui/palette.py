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
