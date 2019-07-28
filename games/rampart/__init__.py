import logging

HEIGHT = 40
WIDTH  = 100
CURSOR_BLOCKED ='▓'
CURSOR_ICON='▒'

count = 0

logging.basicConfig(filename='logs/rampart.log',level=logging.DEBUG)
log = logging.getLogger(__name__)

class NCurses:
        
    def draw_frame(self):
        # top
        self.addstr((-1,-1), '╔══ Rampart ' + '═'*(WIDTH - 11) + '╗')

        # sides
        for y in range(0, HEIGHT+1):
            self.addstr((y,-1), '║' + (' '*WIDTH) + '║')

        # bottom
        self.addstr((HEIGHT,-1), '╚' + ('═'*WIDTH) + '╝')

    def addstr(self, point, msg):
        y = self.offset[0] + point[0]
        x = self.offset[1] + point[1]
        self.stdscr.addstr(y, x, msg)


class RampartPlayer:
    def __init__(self, player):
        self.player = player
        self.cursor = (HEIGHT//2,WIDTH//2)

    def move(self, direction=(-1,0)):
        self.cursor = (
            self.cursor[0] + direction[0], self.cursor[1] + direction[1]
        )
        # print(self.cursor)  # debug show cursor position


class Rampart(NCurses):
    def __init__(self, stdscr, offset=(1,1)):
        self.stdscr = stdscr
        self.offset = offset
        self.players = {}

        self.map = []
        
        for line in range(0,HEIGHT):
            self.map.append([' '] * WIDTH)

    def draw(self):
        self.draw_frame()
        self.draw_map()
        self.draw_players()
        self.thinking()

    def mark(self, point, value=1):
        self.map[point[0]][point[1]] = '█'

    def thinking(self):
        global count
        width = 3
        # Draw a springy bar

        guage = [
            '.. ', ' ..', '. .'
        ]

        if count >= width:
            count = 0

        self.addstr((HEIGHT, WIDTH-4), guage[count])
        count += 1

    def cursor_build(self, player):
        piece = (
          '▓▓▓',
          '▓'
        )

        loc = player.cursor
        y = 0
        x = 0

        for row in piece:
            for val in row:
                self.mark((loc[0]+y, loc[1]+x), 'x')
                x += 1
            y += 1
            x = 0
        
    def cursor_draw(self, player):
        piece = (
          '▓▓▓',
          '▓'
        )

        loc = player.cursor
        x = 0

        for line in piece:
            self.addstr((loc[0]+x, loc[1]), "".join(line))
            x += 1

    def draw_map(self):
        y = 0
        for row in self.map:
            render = ''.join(map(str, row))
            self.addstr((y, 0), render)
            y += 1
        

    def draw_players(self):
        for player in self.players.values():
            self.cursor_draw(player)

    # player/controller
    def add_player(self, player):
        self.players[player] = RampartPlayer(player)
