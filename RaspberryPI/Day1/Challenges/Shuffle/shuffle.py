import sys
import os
sys.path.append(os.path.abspath('../../..')) 

import base64
import time
from utils import animations as anim
ok = 1

while ok:
    answer = int(input("Alegeti o optiune: \n1 Introducere flag\n2 Hint\n"))
    if answer == 2:
        print("\n\nTry to shuffle some words\n\n")
    elif answer == 1:
        flag = input("\n\nIntrodu flag-ul:")
        if flag == base64.b64decode("Y2NjZGRkYWFhZGRkYWJiYWE=".encode('ascii')).decode('ascii'):
            password = base64.b64decode('YmxhY2sgamFjaw=='.encode('ascii')).decode('ascii')
            print("\n\n{}\n\n".format(password))
            anim.display_lock_animation()
            time.sleep(1)
            anim.clear()
            ok = 0
        else:
            print("\n\nWrong flag\n\n")
            anim.display_lock_closed()
            
    else:
        print("\n\nChoose a valid option\n\n")
