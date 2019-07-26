from config import PLAYER_FILE


def all():
    with open(PLAYER_FILE, 'r') as rows:
        players = []

        for row in rows:
            attrs = row.split('\t')
            players.append(Player(*attrs))

        return players


class Player:
    """

    >>> Player(0)

    """

    def __init__(self, name, points=0, contact=None):
        self.name = name
        self.points = int(points)
        self.contact = contact

    @classmethod
    def find(self, name=None):
        for player in all():
            if player.name == name:
                return player


    def scores(self, points=1):
        self.points += points


    def __eq__(self, other):
        return other.name == self.name


    def save(self):
        players = []

        new_player = True

        for player in all():
            if player.name == self.name:
                new_player = False
                players.append(self)
            else:
                players.append(player)

        if new_player:
            players.append(self)

        with open(PLAYER_FILE, 'w') as savefile:
            for player in players:
                savefile.write(player.__repr__() + "\n")

    def __str__(self):
        return "<Player {} score={}>".format(self.name, self.points)


    def __repr__(self):
        return "{}	{}".format(self.name, self.points)


def player(id):
    return players.get(0)
