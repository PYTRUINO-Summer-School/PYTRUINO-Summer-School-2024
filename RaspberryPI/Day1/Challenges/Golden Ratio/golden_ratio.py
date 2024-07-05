import sys
import os
from solution import matrix
sys.path.append(os.path.abspath('../../..')) 

from utils import animations as anim
import base64
import time
ok = 1

password = input('Introdu parola:\n')
if password == base64.b64decode('YmxhY2sgamFjaw=='.encode('ascii')).decode('ascii'):
    while ok:
        answer = int(input("Alegeti o optiune: \n1 Verifica solutia\n2 Hint\n"))
    if answer == 2:
        print("\n\nFibonacci\n\n")
    elif answer == 1:
        if matrix == anim.fibo:
            new_password = base64.b64decode('U2FudGEgQ2xhdXM='.encode('ascii')).decode('ascii')
            print("\n\n{}\n\n".format(password))
            anim.draw_fibonacci_spiral()
            time.sleep(1)
            anim.clear()
            ok = 0
        else:
            print("\n\nTry again\n\n")
            anim.lock_closed()
            
    else:
        print("\n\nChoose a valid option\n\n")
else:
    print("\n\nNu ai gasit parola pentru Challenge\n\n")

