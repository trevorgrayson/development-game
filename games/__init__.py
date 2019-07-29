from games.rampart import Rampart
from games.snake import Snake

from curse import game_runner
from curses import wrapper


GAMES = [
    Rampart,
    Snake
]

def get_game(num):
    return GAMES[num]


def play_game(num):
    Game = get_game(num)
    wrapper(game_runner, Game) 
