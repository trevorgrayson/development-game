import os
from players import Player
from story import story
from messenger import Messenger

COOKIE = os.path.join(os.environ['HOME'], ".dgame")


def cookied_handle():
    if os.path.isfile(COOKIE):
        with open(COOKIE, 'r') as cookie:
            return cookie.read().strip()
        

def challenge(io):
    Messenger.register(io)
    handle = cookied_handle()

    if handle is None:
        handle = io.prompt('login: ').strip()

    player = Player.find(handle)

    if player is None:
        player = Player(handle)

        io.say("Hello new jack. We will need a way to identify you.")
        phrase = io.prompt("Phone Number, email, or passphrase: ")

        player.save()
        io.say("Welcome {}.".format(player.name))
    else: 
        io.say("Welcome back {}.".format(player.name))

    io.say('')
    story(player, io)

    while(True):
        message = io.ask('>')
        message = f"{player} says: {message}."
        Messenger.send(message, io)
