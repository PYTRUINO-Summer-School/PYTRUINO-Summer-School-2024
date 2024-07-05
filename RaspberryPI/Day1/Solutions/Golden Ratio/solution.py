from sense_hat import SenseHat

y = (255, 255, 0) # Yellow
b = (0, 0, 0)     # Black

sense = SenseHat()

matrix = [
   y, y, y, b, y, b, b, y,
   b, b, b, b, y, b, b, b,
   b, b, b, b, y, b, b, b,
   b, b, b, b, b, b, b, b,
   b, y, b, b, b, b, b, b,
   b, b, b, b, b, b, b, b,
   b, b, b, b, b, b, y, b,
   b, b, b, b, b, b, b, b
    ]

def animation()->None:
    sense.set_pixels(matrix)

animation()