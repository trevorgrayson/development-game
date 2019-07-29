from games.rampart import Rampart
from games.snake import Snake


GAMES = [
    Rampart,
    Snake
]

def get_game(num):
    return GAMES[num]

