from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

y = [255, 255, 0]
x = [0, 0, 0]
b = [0, 0, 255]

init_x = 0
init_y = 0

path = [
  y,y,y,x,x,x,x,x,
  x,x,y,x,x,x,x,x,
  x,x,y,x,x,x,x,x,
  x,x,y,y,y,y,y,x,
  x,x,x,x,x,x,y,x,
  x,x,x,x,x,x,y,x,
  x,x,x,x,y,y,y,x,
  x,x,x,x,y,x,x,x
]

while True:
  
  sense.set_pixels(path)
  sense.set_pixel(init_x, init_y, b)
  
  pitch = sense.get_orientation()['pitch'] # rotire pe axa Ox
  roll = sense.get_orientation()['roll']  # rotire pe axa Oz
    
  if 270 < pitch < 315 and init_x < 7:
    init_x += 1

  if 45 < pitch < 90 and init_x > 0:
    init_x -= 1
  
  if 45 < roll < 90 and init_y < 7:
    init_y += 1
  
  if 270 < roll < 315 and init_y > 0:
    init_y -= 1
  
  current = sense.get_pixel(init_x, init_y)
  if current == x:
    init_x = 0
    init_y = 0
  
  sleep(0.4)
  
  