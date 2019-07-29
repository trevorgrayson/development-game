count = 0


class NCurses:
    TITLE = '═══════ '

    def draw_frame(self):
        # top
        self.addstr((-1,-1), '╔═' + self.TITLE.ljust(9,'═') + '═'*(self.width - 10) + '╗')

        # sides
        for y in range(0, self.height+1):
            self.addstr((y,-1), '║' + (' '*self.width) + '║')

        # bottom
        self.addstr((self.height,-1), '╚' + ('═'*self.width) + '╝')


    def addstr(self, point, msg):
        y = self.offset[0] + point[0]
        x = self.offset[1] + point[1]
        self.stdscr.addstr(y, x, msg)


    def thinking(self):
        global count
        width = 3
        # Draw a springy bar

        guage = [
            '.. ', ' ..', '. .'
        ]

        if count >= width:
            count = 0

        self.addstr((self.height, self.width-4), guage[count])
        count += 1


    # player/controller
    def add_player(self, player):
        pass
        #self.players[player] = RampartPlayer(player, (self.height//2, self.width//2))


    def player_action(self, player):
        """Player presses the 'action' key, spacebar"""
        pass

    def tick(self):
        pass
