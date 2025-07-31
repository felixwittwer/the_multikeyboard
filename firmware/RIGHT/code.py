import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from kmk.modules.split import Split, SplitSide
from kmk.modules.steno import Steno, StenoKey
from kmk.modules.layers import Layers
from kmk.modules.oled import OLED
from kmk.modules.oled import OledDisplayMode

keyboard = KMKKeyboard()

keyboard.col_pins = (
    board.IO04, board.IO05, board.IO06, board.IO07,
    board.IO08, board.IO09, board.IO10, board.IO11, 
    board.IO12, board.IO13, board.IO14, board.IO15
)
keyboard.row_pins = (
    board.IO16, board.IO17, board.IO18, board.IO21,
    board.IO35, board.IO36
)
keyboard.diode_orientation = DiodeOrientation.ROW2COL

keyboard.modules.append(Layers())

oled = OLED(
    oled_addr=0x3C,
    sda=board.IO37,
    scl=board.IO38,
    i2c_bus=1,
    display_mode=OledDisplayMode.SPLIT,
    flip=False,
)
keyboard.modules.append(oled)

split = Split(
    split_side=SplitSide.RIGHT,
    uart_tx=board.IO2,
    uart_rx=board.IO1,
    use_pio=True,
)
keyboard.modules.append(split)

keyboard.modules.append(Steno())

keyboard.keymap = [
    [
        KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.PSCR, KC.INS, KC.DEL, KC.ASTR, KC.NLCK, KC.ESC, None
        KC.N7, KC.N8, KC.N9, KC.N0, KC.MINS, KC.EQL, KC.BSPC, KC.NUBS, KC.SLSH, KC.N7, KC.N8, KC.N9
        KC.Z, KC.U, KC.I, KC.O, KC.P, KC.UDIA, KC.PLUS, KC.ENT, KC.PPLS, KC.N4, KC.N5, KC.N6
        KC.H, KC.J, KC.K, KC.L, KC.ODIA, KC.ADIA, KC.RSFT, KC.UP, KC.MINS, KC.N1, KC.N2, KC.N3
        KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.MINS, KC.LEFT, KC.DOWN, KC.RIGHT, KC.N0, KC.COMM, KC.PENT
        KC.SPC, KC.SPC, KC.SPC, KC.RALT, KC.MPRV, KC.RCTL, None, None, None, None, None, None,
    ],
    [
        None, None, None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None, None, None,
        StenoKey('*'), StenoKey('F-'), StenoKey('P-'), StenoKey('L-'), StenoKey('T-'), StenoKey('D-'), None, None, None, None, None, None,
        StenoKey('*'), StenoKey('R-'), StenoKey('B-'), StenoKey('G-'), StenoKey('S-'), StenoKey('Z-'), None, None,None, None, None, None,
        None, None, None, None, None, None, None, None, None, None, None, None,
        StenoKey('E-'), StenoKey('U-'), None, None, None, None, None, None, None, None, None, None,
    ],
]

if __name__ == '__main__':
    keyboard.go()
