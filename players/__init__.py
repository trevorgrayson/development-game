
def all():
    with open('players.bin', 'r') as rows:
        players = []

        for row in rows:
            attrs = row.split('\t')
            players.append(Player(*attrs))

        return players


class Player:
    """

    >>> Player(0)

    """

    def __init__(self, name, points=0):
        self.name = name
        self.points = int(points)

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

        for player in all():
            if player == self:
                players.append(self)
            else:
                players.append(player)

        with open('players.bin', 'w') as savefile:
            for player in players:
                savefile.write(player.__repr__() + "\n")

    def __str__(self):
        return "<Player {} score={}>".format(self.name, self.points)


    def __repr__(self):
        return "{}	{}".format(self.name, self.points)


def player(id):
    return players.get(0)
