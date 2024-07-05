from sense_hat import SenseHat
import time

sense = SenseHat()

# Define colors
r = (255, 0, 0)  # Red
g = (0, 255, 0)
b = (0, 0, 0)    # Black

# Define the closed lock icon pattern
lock_closed = [
    b, b, b, r, r, b, b, b,
    b, b, r, b, b, r, b, b,
    b, r, b, b, b, b, r, b,
    b, r, r, r, r, r, r, b,
    b, r, r, r, r, r, r, b,
    b, r, r, r, r, r, r, b,
    b, r, r, r, r, r, r, b,
    b, b, b, b, b, b, b, b
]

lock_open = [
    b, b, b, g, g, b, b, b,
    b, b, g, b, b, b, b, b,
    b, g, b, b, b, b, b, b,
    b, g, g, g, g, g, g, b,
    b, g, g, g, g, g, g, b,
    b, g, g, g, g, g, g, b,
    b, g, g, g, g, g, g, b,
    b, b, b, b, b, b, b, b
]

# Function to display the lock animation
def display_lock_closed():
    for i in range(3):
        sense.set_pixels(lock_closed)
        time.sleep(0.5)
        sense.clear()
        time.sleep(0.5)
    sense.set_pixels(lock_closed)

def display_lock_animation():
    # Show closed lock
    sense.set_pixels(lock_closed)
    time.sleep(1)
    # Show open lock
    sense.set_pixels(lock_open)

def clear():
    sense.clear()

