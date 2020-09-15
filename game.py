from sys import exit
from random import randint
from textwrap import dedent

import scenes

a_map = Map('home')
a_game = Engine(a_map)
a_game.play()
