BLANK_SQR = ' '


class BoardPlayer:
    """
    `players.Player` wrapper that gives positioning and actions.
    """
    def __init__(self, player, cursor=(0,0), direction=(1,0)):
        self.player = player
        self.cursor = cursor
        self.direction = direction
