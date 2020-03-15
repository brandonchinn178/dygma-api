"""Generate the color map specified by a palette and layer."""

from typing import List, Optional

from .keys import Key
from .layer import Layer


def get_colormap(palette: List[str], layer: Layer) -> List[int]:
    """Get the colormap as specified by the given palette and layer."""
    return [_get_layer_key_color_code(palette, layer, key) for key in KEY_MAP]


def _get_layer_key_color_code(
    palette: List[str], layer: Layer, key: Optional[Key]
) -> int:
    if key is None:
        color = None
    else:
        layer_key = layer.keymap.get(key, layer.default_key)
        color = layer_key.color

    if color is None:
        color = layer.base_color

    return palette.index(color)


# The order of keys in a Dygma color map
# `None` indicates a key that should always be the base color (e.g. neuron)
KEY_MAP = [
    Key.ESC,
    Key.ONE,
    Key.TWO,
    Key.THREE,
    Key.FOUR,
    Key.FIVE,
    Key.SIX,
    Key.TAB,
    Key.Q,
    Key.W,
    Key.E,
    Key.R,
    Key.T,
    Key.CAPS_LOCK,
    Key.A,
    Key.S,
    Key.D,
    Key.F,
    Key.G,
    Key.LSHIFT,
    Key.ALT_BACKSLASH,
    Key.Z,
    Key.X,
    Key.C,
    Key.V,
    Key.B,
    Key.LCTRL,
    Key.LGUI,
    Key.LALT,
    Key.LSPACE_NW,
    Key.LSPACE_NE,
    Key.LSPACE_SW,
    Key.LSPACE_SE,
    Key.BACKSPACE,
    Key.EQUAL,
    Key.MINUS,
    Key.ZERO,
    Key.NINE,
    Key.EIGHT,
    Key.SEVEN,
    Key.ENTER,
    Key.RBRACK,
    Key.LBRACK,
    Key.P,
    Key.O,
    Key.I,
    Key.U,
    Key.Y,
    Key.BACKSLASH,
    Key.QUOTE,
    Key.SEMICOLON,
    Key.L,
    Key.K,
    Key.J,
    Key.H,
    Key.RSHIFT,
    Key.SLASH,
    Key.PERIOD,
    Key.COMMA,
    Key.M,
    Key.N,
    Key.RCTRL,
    Key.RGUI,
    Key.FN,
    Key.RALT,
    Key.RSPACE_NE,
    Key.RSPACE_NW,
    Key.RSPACE_SE,
    Key.RSPACE_SW,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
]
