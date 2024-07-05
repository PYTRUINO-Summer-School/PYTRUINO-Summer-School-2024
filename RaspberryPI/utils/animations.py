from sense_hat import SenseHat
import time

sense = SenseHat()

# Define colors
r = (255, 0, 0)  # Red
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

# Define the partially open lock icon pattern
lock_opening = [
    b, b, b, r, r, b, b, b,
    b, r, r, b, b, r, r, b,
    b, r, b, b, b, b, r, b,
    b, b, r, r, r, r, b, b,
    b, b, b, r, r, b, b, b,
    b, b, b, r, r, b, b, b,
    b, b, b, r, r, b, b, b,
    b, b, b, b, b, b, b, b
]

lock_open = [
    b, b, b, b, b, b, b, b,
    b, r, r, b, b, r, r, b,
    b, r, b, b, b, b, r, b,
    b, b, b, r, r, b, b, b,
    b, b, b, r, r, b, b, b,
    b, b, b, r, r, b, b, b,
    b, b, b, r, r, b, b, b,
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
    # Show opening stages
    for _ in range(3):
        sense.set_pixels(lock_opening)
        time.sleep(0.5)
        sense.set_pixels(lock_closed)
        time.sleep(0.5)
    # Show open lock
    sense.set_pixels(lock_open)

