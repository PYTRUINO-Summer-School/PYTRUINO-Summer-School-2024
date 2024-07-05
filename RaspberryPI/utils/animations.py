from sense_hat import SenseHat
import time
import math

sense = SenseHat()

# Define colors
r = (255, 0, 0)   # Red
g = (0, 255, 0)   # Green
b = (0, 0, 0)     # Black
y = (255, 255, 0) # Yellow

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

fibo = [
   y, y, y, b, y, b, b, y,
   b, b, b, b, y, b, b, b,
   b, b, b, b, y, b, b, b,
   b, b, b, b, b, b, b, b,
   b, y, b, b, b, b, b, b,
   b, b, b, b, b, b, b, b,
   b, b, b, b, b, b, y, b,
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

def plot_point(x, y, color):
    if 0 <= x < 8 and 0 <= y < 8:
        sense.set_pixel(x, y, color)

def draw_fibonacci_spiral():
    # Initial values for the Fibonacci sequence
    a, b = 0, 1
    x, y = 4, 4  # Start from the center of the matrix

    # Clear the display
    sense.clear()

    for i in range(8):
        # Calculate the next point in the Fibonacci sequence
        a, b = b, a + b
        angle = math.radians(i * 90)  # Rotate by 90 degrees each step
        
        # Calculate the end point of the segment
        end_x = x + int(b * math.cos(angle))
        end_y = y + int(b * math.sin(angle))

        # Draw the line segment
        plot_point(x, y, y)
        plot_point(end_x, end_y, y)

        # Move to the next starting point
        x, y = end_x, end_y

        # Pause for a moment to create an animation effect
        time.sleep(0.5)
    

