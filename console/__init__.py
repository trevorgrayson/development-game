from players import Player


def challenge():
    handle = input('login: ')

    player = Player.find(handle)

    if player is None:
        player = Player(handle)

        print("Hello new jack. We will need a way to identify you.")
        phrase = input("Phone Number, email, or passphrase: ")

        player.save()
        print("Welcome {}.".format(player.name))
    else: 
        print("Welcome back {}.".format(player.name))
        
