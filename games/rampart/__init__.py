import logging
from curse.base import NCurses
from games.base import BoardPlayer, BLANK_SQR

CURSOR_BLOCKED ='▓'
CURSOR_ICON='▒'

logging.basicConfig(filename='logs/rampart.log',level=logging.DEBUG)
log = logging.getLogger(__name__)


class RampartPlayer(BoardPlayer):
    """
    `players.Player` wrapper that gives positioning and actions.
    """
    def move(self, direction=(-1,0)):
        """ 
        direction: two digit vector telling which direction will be moved in.
        """
        self.cursor = (
            self.cursor[0] + direction[0], self.cursor[1] + direction[1]
        )
        # print(self.cursor)  # debug show cursor position


class Rampart(NCurses):
    TITLE = 'rampart'

    width = 100
    height = 20

    def __init__(self, stdscr, offset=(1,1)):
        self.stdscr = stdscr
        self.offset = offset
        self.players = {}

        self.map = []
        
        for line in range(0,self.height):
            self.map.append([BLANK_SQR] * self.width)


    def tick(self):
        self.draw_frame()
        self.draw_map()
        self.draw_players()


    def mark(self, point, value='█'):
        self.map[point[0]][point[1]] = value


    def player_action(self, player):
        piece = (
          '▒▒▒',
          '▒'
        )

        loc = player.cursor
        y = 0
        x = 0

        for row in piece:
            for val in row:
                self.mark((loc[0]+y, loc[1]+x), CURSOR_BLOCKED)
                x += 1
            y += 1
            x = 0
        

    def cursor_draw(self, player):
        piece = (
          '▒▒▒',
          '▒'
        )

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
        self.players[player] = RampartPlayer(player, (self.height//2, self.width//2))


    def draw_players(self):
        for player in self.players.values():
            self.cursor_draw(player)
