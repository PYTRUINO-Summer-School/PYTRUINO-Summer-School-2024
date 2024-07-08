from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

r = (255, 0, 0)
bl = (0, 0, 0)
w = (255, 255, 255)
b = (0, 0, 255)
g = (0, 255, 0)

ok = True
while ok:
    for event in sense.stick.get_events():
        # Verificam daca avem una din taste apasate
        if event.action == "pressed":

            # Verificam care dintre sageti este apasata
            if event.direction == "up":
                # afisam temperatura
                temperature_value = sense.get_temperature()
                sense.show_message("Temperatura curenta este: {}".format(temperature_value), text_colour=r, back_colour=w)
                sense.clear()
            elif event.direction == "down":
                # afisam umidiatatea
                humidity_value = sense.get_humidity()
                sense.show_message("Umiditatea curenta este: {}".format(humidity_value), text_colour=b, back_colour=w)
                sense.clear()
            elif event.direction == "left":
                # afisam presiunea
                pressure_value = sense.get_pressure()
                sense.show_message("Presiunea curenta este: {}".format(pressure_value), text_colour=g, back_colour=w)
                sense.clear()
            elif event.direction == "right":
                # cand vom apasa tasta dreapta programul se va inchide
                ok=0

sense.show_message("Programul s-a inchis cu succes", text_colour = bl, back_colour=w)
sense.clear()

