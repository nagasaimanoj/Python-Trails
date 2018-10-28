from threading import Thread


class myThread(Thread):
    def __init__(self, threadID):
        Thread.__init__(self)
        self.id = threadID

    def run(self):
        while True:
            print("     " * self.id, self.id)


for i in range(10):
    myThread(i).start()
