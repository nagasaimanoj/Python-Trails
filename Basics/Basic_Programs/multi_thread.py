import threading


class myThread (threading.Thread):

    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.id = threadID

    def run(self):
        for i in range(100):
            for j in range(self.id):
                print("     ", end=" ")
            print(self.id)


myThread(1).start()
myThread(2).start()
