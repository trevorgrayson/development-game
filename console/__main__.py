from . import challenge


class IO:
    def say(self, msg):
        print(msg)

    def prompt(self, msg):
        return input(msg)

    def ask(self, msg):
        return self.prompt(msg)

while(True):
		challenge(IO())
