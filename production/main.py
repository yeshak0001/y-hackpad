import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys


keyboard = KMKKeyboard()

# Macros
macros = Macros()
keyboard.modules.append(macros)

# Media keys (VOLU/VOLD/MUTE)
keyboard.modules.append(MediaKeys())

# --- Your 4 button pins (update these to match your wiring/PCB) ---
# For XIAO RP2040, these are common choices (A0-A3 are GP26-GP29).
PINS = [board.GP26, board.GP27, board.GP28, board.GP29]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,  # typical when switches go to GND
)

# --- Rotary encoder pins (update these to match your wiring/PCB) ---
# Encoder pins: A, B, and the push switch pin (button).
ENC_A = board.GP0
ENC_B = board.GP1
ENC_SW = board.GP7  # encoder press -> mute

encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

# (pin_a, pin_b, pin_button, [optional invert], [optional divisor])
encoder_handler.pins = ((ENC_A, ENC_B, ENC_SW, False),)

# Per-layer mapping: (CCW, CW, PRESS) for each encoder
encoder_handler.map = (
    ((KC.VOLD, KC.VOLU, KC.MUTE),),
)

keyboard.keymap = [
    [
        KC.A,
        KC.DELETE,
        KC.MACRO("Hello world!"),
        KC.MACRO(
            Press(KC.LCMD),
            Tap(KC.S),
            Release(KC.LCMD),
        ),
    ]
]

if __name__ == "__main__":
    keyboard.go()
