#parent class
class Enemy(object):

    def move_left(self):
        print('Moving left...')

    def move_right(self):
        print('Moving right...')

#child class
class Ninja(Enemy):

    def karate_chop(self):
        print('Karate chop!')

#child class
class Zombie(Enemy):

    def bite(self):
        print('I am biting you!')

#parent class object
enemy = Enemy()
enemy.move_left()

#child class object
ninja = Ninja()
ninja.move_left()
ninja.karate_chop()

#child class object
zombie = Zombie()
zombie.move_right()
zombie.bite()