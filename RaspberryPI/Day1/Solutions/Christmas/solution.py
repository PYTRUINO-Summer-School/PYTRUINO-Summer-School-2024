from sense_hat import SenseHat
sense = SenseHat()

import time

def draw_something():
    g = (0, 255, 0)
    br = (87, 55, 0)
    r = (255, 0, 0)
    w = (255, 255, 255)
    y = (255, 255, 0)
    bl = (0, 0, 0)

    christmas_tree = [
        w, w, w, w, w, w, w, w,
        w, w, w, y, g, w, w, w,
        w, w, r, g, w, g, w, w,
        w, y, g, g, y, g, y, w,
        g, r, g, g, g, g, r, g,
        w, w, w, br, br, w, w, w,
        w, w, w, br, br, w, w, w,
        w, w, w, br, br, w, w, w,
    ]

    christmas_tree_gift = [
        w, w, w, w, w, w, w, w,
        g, w, w, w, w, w, w, w,
        w, g, w, w, w, w, w, w,
        y, g, y, w, w, w, w, w,
        g, g, r, g, w, w, w, w,
        br, w, w, w, w, r, y, r,
        br, w, w, w, w, y, r, y,
        br, w, w, w, w, r, y, r,
    ]

    santa = [
        r, r, r, r, bl, bl, bl, bl,
        r, r, r, r, r, bl, bl, bl,
        w, w, r, r, r, bl, bl, bl,
        w, w, r, r, r, r, bl, bl,
        bl, bl, r, r, r, r, r, bl,
        bl, r, r, r, r, r, r, bl,
        r, r, r, r, r, r, r, r,
        w, w, w, w, w, w, w, w,
    ]

    sense.set_pixels(christmas_tree)
    time.sleep(1.5)
    sense.set_pixels(christmas_tree_gift)
    time.sleep(1.5)
    sense.set_pixels(santa)
    time.sleep(1.5)
    sense.clear()
    
    sense.show_message("Merry Christmas!", text_colour=r, back_colour=w)



    