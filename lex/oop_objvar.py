class Robot:

    population = 0

    def __init__(self, name):
        self.name = name
        Robot.population += 1
        print('A new robot is born! Its name is ', self.name)

    def die(self):
        Robot.population -= 1
        if Robot.population == 0:
            print('the last robot die. Its name is', self.name)
        else:
            print('there are still {:d} robots alive'.format(Robot.population))

    @classmethod
    def count(cls):
        print('The population is ', cls.population)


Jimmy = Robot('Jimmy')
Jimmy.die()
Robot.count()
Jack = Robot('Jack')
May = Robot('May')
Robot.count()
May.die()
Jack.die()
