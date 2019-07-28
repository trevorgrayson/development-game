import time
import curses
from games.rampart import Rampart


def main(stdscr):
    # Make stdscr.getch non-blocking
    stdscr.nodelay(True)
    stdscr.clear()

    stdscr.keypad(True)
    # curses.echo()
    curses.cbreak()

    player = 1

    rampart = Rampart(stdscr)
    rampart.add_player(player)
    player = rampart.players[player]


    while True:
        c = stdscr.getch()

        if c == curses.KEY_UP: player.move((-1,0))
        elif c == curses.KEY_DOWN: player.move((1,0))
        elif c == curses.KEY_LEFT: player.move((0,-1))
        elif c == curses.KEY_RIGHT: player.move((0,1))
        elif c == ord('b'): rampart.cursor_build(player)

        # Clear out anything else the user has typed in
        curses.flushinp()
        stdscr.clear()

        rampart.draw()

        time.sleep(0.1)
