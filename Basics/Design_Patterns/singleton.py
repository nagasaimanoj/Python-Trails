class Singleton(object):
    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print('Instance does not exist...')
        else:
            print('Instance exists:', self.get_instance())

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


a = Singleton()

print('Creating instance', Singleton.get_instance())

b = Singleton()
c = Singleton()
