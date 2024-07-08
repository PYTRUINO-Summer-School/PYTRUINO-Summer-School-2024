from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

y = (255, 255, 0)
bl = (0, 0, 0)
b = (0, 0, 255)

init_x = 0
init_y = 0

path = [
  y,  y,  y,  bl, bl, bl, bl, bl,
  bl, bl, y,  y,  bl, bl, bl, bl,
  bl, bl, bl, y,  bl, bl, bl, bl,
  bl, bl, bl, y,  y,  y,  bl, bl,
  bl, bl, bl, bl, bl, y,  y,  bl,
  bl, bl, bl, bl, bl, bl, y,  y,
  bl, bl, bl, bl, bl, bl, bl, y,
  bl, bl, bl, bl, y,  y,  y,  y
]

while True:
  sense.set_pixels(path)
  sense.set_pixel(init_x, init_y, b)

  pitch = sense.get_orientation()['pitch'] # rotirea pe axa x
  roll = sense.get_orientation()['roll']   # rotirea pe axa z

  print('Pitch:', pitch)
  print('Roll:', roll)

  if 270 < pitch < 315 and init_x < 7:
    init_x += 1

  if 45 < pitch < 90 and init_x > 0:
    init_x -= 1

  if 45 < roll < 90 and init_y < 7:
    init_y += 1

  if 270 < roll < 315 and init_y > 0:
    init_y -= 1

  current = sense.get_pixel(init_x, init_y)
  if current == bl:
    init_x = 0
    init_y = 0

  if init_x == 4 and init_y == 7:
    sense.clear()
    sense.show_message("Winner!", text_colour=b, back_colour=y)
    sense.clear()
    break

  sleep(0.4)