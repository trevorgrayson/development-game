from . import challenge


class IO:
    def say(self, msg):
        print(msg)

    def prompt(self, msg):
        return input(msg)


while(True):
		challenge(IO())
