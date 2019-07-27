from players import Player


def challenge(io):
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
