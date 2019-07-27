MESSAGES = []
SUBSCRIBERS = []


class Messenger:

    @classmethod
    def send(cls, msg, sender=None):

        global SUBSCRIBERS
        for sub in SUBSCRIBERS:
            if sender == sub:
                continue

            sub.say(msg)

    @classmethod
    def messages(cls):
        global MESSAGES
        for msg in MESSAGES:
            yield msg

    @classmethod
    def register(cls, io):
        global SUBSCRIBERS
        SUBSCRIBERS.append(io)
