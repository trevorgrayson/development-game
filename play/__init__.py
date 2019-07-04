import json
from players import Player, all

def score_board(players):
    for player in players:
        print(player)


def play():
    tg = Player.find('tg')
    tg.scores(1)
    tg.scores(1)
    tg.save()

    score_board(all())


if __name__ == '__main__':
    play()
