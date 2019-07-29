import sys
from . import main
from curses import wrapper
from games import get_game


Game = None

try:
    num = int(sys.argv[1])
    Game = get_game()

except IndexError:
    print("unknown game, picking 1.")
    Game = get_game(1)
    # print list of games
# _curses.error: addwstr() returned ERR  => made the field too big?


wrapper(main, Game) 
