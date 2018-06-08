class Publisher():
    users = set()

    def register(self, user):
        self.users.add(user)

    def unregister(self, user):
        self.users.discard(user)

    def send_notifications(self, message):
        for user in self.users:
            user.notify(message)


class Subscriber():
    def __init__(self, username):
        self.username = username

    def notify(self, message):
        print(self.username, 'received message:', message)


publisher = Publisher()

bucky = Subscriber('Bucky')
manoj = Subscriber('Manoj')
publisher.register(bucky)
publisher.register(manoj)

publisher.send_notifications('We updated the website')
publisher.send_notifications('Make sure to add a profile picture')
