import sys
from . import main
from curses import wrapper
from games import get_game


Game = None

try:
    num = int(1)
    Game = get_game(num)
except Exception:
    print("unknown game: %s" % sys.argv[1])
    # print list of games

wrapper(main, Game) 
