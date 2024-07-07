import sys
import os
from solution import draw_something
sys.path.append(os.path.abspath('../../..')) 

from utils import animations as anim
import base64
import time
ok = 1

password = input('Introdu parola:\n')
if password == base64.b64decode('U2FudGEgQ2xhdXM='.encode('ascii')).decode('ascii'):
    draw_something()

