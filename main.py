def on_button_pressed_b():
    for index in range(100):
        basic.show_leds("""
            # . # . #
            . # . # .
            # . # . #
            . # . # .
            # . # . #
            """)
        basic.show_leds("""
            . # . # .
            # . # . #
            . # . # .
            # . # . #
            . # . # .
            """)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    pass
basic.forever(on_forever)
