class Enemy(object):

    def move_left(self):
        print('Moving left...')

    def move_right(self):
        print('Moving right...')

class Ninja(Enemy):

    def karate_chop(self):
        print('Karate chop!')

class Zombie(Enemy):

    def bite(self):
        print('I am biting you!')

enemy = Enemy()
enemy.move_left()

ninja = Ninja()
ninja.move_left()
ninja.karate_chop()

zombie = Zombie()
zombie.move_right()
zombie.bite()
