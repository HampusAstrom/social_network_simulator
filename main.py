import random as rng

class Person:
    def __init__(self, name):
        self.name = name
        self.__init_traits()
        self.energy = rng.uniform(0,100)
        self.happiness = rng.uniform(0,100)
        self.loneliness = rng.uniform(0,100)
        self.events_attended = 0

    def __init_traits(self):
        self.personality = {}
        self.personality['extroversion'] = rng.gauss(0,1)

    def assess_attendance(self, event):
        score = self.energy
        score += self.loneliness * 2
        score /= 300 # should now be between 0-1
        score += self.personality['extroversion'] * 0.3
        if score > rng.uniform(0, 1):
            return True
        else:
            return False

    def print_state(self):
        print('{}:\tenergy = {:6.2f},\thappiness = {:6.2f},\tloneliness = {:6.2f}'.format(self.name,
            self.energy, self.happiness, self.loneliness))

    def print_personality(self):
        print('{}:'.format(self.name), end='\t')
        for trait, value in self.personality.items():
            print('{} = {:6.2f}'.format(trait, value), end='\t')
        print()

def main():
    people = {'Adam': Person('Adam'), 'Beth': Person('Beth'), 'Clare': Person('Clare')}
    dummy_event = ''
    for i in range(100):
        print ('Event {}'.format(i))
        for name, person in people.items():
            if person.assess_attendance(dummy_event):
                print('{} attends event'.format(name))
                person.events_attended += 1

    print()
    for name, person in people.items():
        person.print_state()
        person.print_personality()
        print('{} attended {} events'.format(name, person.events_attended))
        print()


if __name__ == '__main__':
    main()
