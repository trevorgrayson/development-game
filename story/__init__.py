import time
import random
from messenger import Messenger
from .locations import LOCATIONS


def story(player, io):
    location = LOCATIONS[random.choice(list(LOCATIONS.keys()))]
    io.say("You find yourself in an familiar location.  "
          f"It appears to be {location}.")

    if location.mayor:
        io.say(f"{location.mayor} is the mayor of these lands, you should be respectful.")

        # list of things that will 
        # leave a mark or not
        # be respectful or disrespect
    else:
        io.say(f"No one seems to be here.")
