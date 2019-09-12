import time
import curses

SPACE_BAR = 32

TICK = 0.1

def game_runner(stdscr, Game):
    # Make stdscr.getch non-blocking
    stdscr.nodelay(True)
    stdscr.clear()

    stdscr.keypad(True)
    curses.curs_set(False)
    # curses.echo()
    curses.cbreak()

    player = 1

    game = Game(stdscr)
    game.add_player(player)
    player = game.players[player]

    # stdscr.clear()

    game.tick()

    while True:
        c = stdscr.getch()

        if   c == curses.KEY_UP:    player.move((-1, 0))
        elif c == curses.KEY_DOWN:  player.move((1, 0))
        elif c == curses.KEY_LEFT:  player.move((0, -1))
        elif c == curses.KEY_RIGHT: player.move((0, 1))
        elif c == SPACE_BAR: game.player_action(player)

        # Clear out anything else the user has typed in
        # curses.flushinp()

        game.tick()

        time.sleep(TICK)
