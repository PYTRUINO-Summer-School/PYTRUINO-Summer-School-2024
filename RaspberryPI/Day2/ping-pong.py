from time import sleep
from sense_hat import SenseHat
sense = SenseHat()

init_y = 4

b = (0, 0, 255)
w = (255, 255, 255)

ball_position = [3, 3]
ball_velocity = [1, 1]

"""
In matricea de led-uri indicii x si y merg diferit fata de o matrice normala.
    - pentru x, 0 este cel mai din stanga led si pentru 7 este cel mai din dreapta
    - pentru y, 0 este cel mai de sus led si 7 cel mai de jos
Practic indicii sunt inversati fata de cum ar fi normal intr-o matrice
    
"""

def draw_player():
    sense.set_pixel(0, init_y, w)
    sense.set_pixel(0, init_y+1, w)
    sense.set_pixel(0, init_y-1, w)

def move_up(event):
    global init_y
    if init_y > 1 and event.action=='pressed':
        init_y -= 1
    print(event)

def move_down(event):
    global init_y
    if init_y < 6 and event.action=='pressed':
       init_y += 1
    print(event)

def draw_ball():
    sense.set_pixel(ball_position[0], ball_position[1],b)
    ball_position[0] += ball_velocity[0]
    ball_position[1] += ball_velocity[1]
    if ball_position[0] == 7:
        ball_velocity[0] = -ball_velocity[0]
    if ball_position[1] == 0 or ball_position[1] == 7:
        ball_velocity[1] = -ball_velocity[1]
    if ball_position[0] == 0:
        sense.show_message("You Lose", text_colour=(255, 0, 0))
        quit()
    if ball_position[0] == 1 and init_y - 1 <= ball_position[1] <= init_y+1:
        ball_velocity[0] = -ball_velocity[0]

# pentru o anumita actiune de pe joystick o sa apelam o anumita functie
sense.stick.direction_up = move_up  # atunci cand mutam joystick-ul in sus apelam move_up()
sense.stick.direction_down = move_down  # atunci cand mutam joystick-ul in jos apelam move_down()

while True:
    sense.clear()
    draw_player()
    draw_ball()
    sleep(0.25)