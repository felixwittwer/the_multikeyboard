import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from kmk.modules.split import Split, SplitSide
from kmk.modules.encoder import EncoderHandler
from kmk.modules.steno import Steno, StenoKey
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
from kmk.handlers.sequences import simple_key_sequence, macro

keyboard = KMKKeyboard()

keyboard.col_pins = (
    board.IO04, board.IO05, board.IO06, board.IO07, board.IO08,
    board.IO09, board.IO10, board.IO11, board.IO12, board.IO13
)
keyboard.row_pins = (
    board.I14, board.I15, board.I16,
    board.I17, board.I18, board.I21,
)
keyboard.diode_orientation = DiodeOrientation.ROW2COL

keyboard.modules.append(Layers())

split = Split(
    split_side=SplitSide.LEFT,
    uart_tx=board.IO1,
    uart_rx=board.IO2,
    use_pio=True,
)
keyboard.modules.append(split)

encoder_handler = EncoderHandler()
encoder_handler.pins = [
    (board.IO35, board.IO36),
    (board.IO47, board.IO48),
]
encoder_handler.map = [
    ((KC.VOLD, KC.VOLU), (KC.LEFT, KC.RIGHT)),
]
keyboard.modules.append(encoder_handler)

keyboard.modules.append(Steno())
keyboard.extensions.append(MediaKeys())

M00 = KC.NO
M01 = macro(simple_key_sequence((KC.LCTL, KC.C)))
M02 = KC.NO
M03 = KC.NO
M04 = macro(simple_key_sequence((KC.LCTL, KC.V)))  # Paste
M05 = macro(simple_key_sequence((KC.LCTL, KC.Z)))  # Undo
M06 = macro(simple_key_sequence((KC.LCTL, KC.Y)))  # Redo
M07 = macro(simple_key_sequence((KC.LCTL, KC.X)))  # Cut
M08 = KC.NO
M09 = KC.NO
M10 = KC.NO
M11 = KC.NO
M12 = KC.NO
M13 = KC.NO
M14 = KC.NO
M15 = KC.NO

keyboard.keymap = [
    [
        None, None, None, KC.TG(1), KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6,
        None, None, None, KC.ESC, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6,
        M00, M01, M02, M03, KC.GRV, KC.Q, KC.W, KC.E, KC.R, KC.T,
        M04, M05, M06, M07, KC.TAB, KC.A, KC.S, KC.D, KC.F, KC.G,
        M08, M09, M10, M11, KC.LSFT, KC.LSFT, KC.Y, KC.X, KC.C, KC.V,
        M12, M13, M14, M15, KC.LCTL, KC.RGUI, KC.LALT, KC.SPC, KC.SPC, KC.SPC,
    ],
    [
        None, None, None, KC.TG(1), None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, StenoKey('S-'), StenoKey('T-'), StenoKey('P-'), StenoKey('H-'), StenoKey('*'),
        None, None, None, None, None, StenoKey('S-'), StenoKey('K-'), StenoKey('W-'), StenoKey('R-'), StenoKey('*'),
        None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, StenoKey('A-'), StenoKey('O-'), StenoKey('*'),
    ],
]

if __name__ == '__main__':
    keyboard.go()
