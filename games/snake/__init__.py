import numpy as np
import logging

from curse.base import NCurses
from games.base import BoardPlayer, BLANK_SQR

CURSOR_BLOCKED ='▓'
CURSOR_ICON='▒'

logging.basicConfig(filename='logs/snake.log',level=logging.DEBUG)
log = logging.getLogger(__name__)


class SnakePlayer(BoardPlayer):
    """
    `players.Player` wrapper that gives positioning and actions.
    """

    tail = [(0,0), (0,0), (0,0), (0,0), (0,0)]

    def move(self, direction=(-1,0)):
        """ 
        direction: two digit vector telling which direction will be moved in.
        """
        direction = np.array(direction)
        diff = np.array(self.direction) - direction
        if not (diff[0] > 1 or diff[1] > 1 or diff[0] < -1 or diff[1] < -1):
            self.direction = direction


    def tick(self):
        self.cursor = (
            self.cursor[0] + self.direction[0],
            self.cursor[1] + self.direction[1]
        )

        self.tail_tip = self.tail.pop(0)  # to be killed
        self.tail.append(self.cursor)


class Snake(NCurses):
    TITLE = 'snake' 

    width = 100
    height = 40

    def __init__(self, stdscr, offset=(1,1)):
        self.stdscr = stdscr
        self.offset = offset
        self.players = {}

        self.map = []
        
        for line in range(0,self.height):
            self.map.append([' '] * self.width)

    def tick(self):
        for _, player in self.players.items():
            player.tick()

        self.draw_frame()
        self.draw_map()
        self.draw_players()

    def mark(self, point, value='█'):
        self.map[point[0]][point[1]] = value
        
    def cursor_draw(self, player):
        piece = '▓'

        loc = player.cursor
        x = 0

        for line in piece:
            self.addstr((loc[0]+x, loc[1]), ''.join(line))
            x += 1

    def draw_map(self):
        y = 0
        for row in self.map:
            render = ''.join(map(str, row))
            self.addstr((y, 0), render)
            y += 1

    def add_player(self, player):
        self.players[player] = SnakePlayer(player, (self.height//2, self.width//2))
        
    def draw_players(self):
        for player in self.players.values():
            self.cursor_draw(player)

            
            self.mark(player.tail_tip, BLANK_SQR)
            for segment in player.tail:
                self.mark(segment)
