import random as rng

people = {}

def clamp(x, bot = 0, top = 100):
    x = max(x, bot)
    return min(x, top)

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

    def home_alone(self):
        n_energy = clamp(self.energy + 2 - self.personality['extroversion'])
        self.loneliness = clamp(self.loneliness + 2 + max(-1, self.personality['extroversion']))
        n_happiness = clamp(self.happiness - self.loneliness * 0.1)
        self.energy = n_energy
        self.happiness = n_happiness

    def experience_event(self, num_attend):
        n_energy = clamp(self.energy - num_attend * 0.2 + self.personality['extroversion'])
        self.loneliness = clamp(self.loneliness - 2)
        n_happiness = clamp(self.happiness + 2 - self.loneliness * 0.05)
        self.energy = n_energy
        self.happiness = n_happiness

    def score(self):
        return (self.energy/100)*(self.happiness/100)*(1-self.loneliness/100)

    def print_state(self):
        print('{}:\tenergy = {:6.2f},\thappiness = {:6.2f},\tloneliness = {:6.2f}'.format(self.name,
            self.energy, self.happiness, self.loneliness))

    def print_personality(self):
        print('{}:'.format(self.name), end='\t')
        for trait, value in self.personality.items():
            print('{} = {:6.2f}'.format(trait, value), end='\t')
        print()

class Event:
    def __init__(self):
        self.attendees = {}

    def attend(self, name, person):
        self.attendees[name] = person

    def occur(self):
        num = len(self.attendees)
        for name, person in self.attendees.items():
            person.experience_event(num)

def main():
    people = {'Adam': Person('Adam'), 'Beth': Person('Beth'), 'Clare': Person('Clare')}
    for i in range(100):
        event = Event()
        print ('Event {}'.format(i))
        for name, person in people.items():
            print('{} has score {} before event.'.format(name, person.score()), end=' ')
            if person.assess_attendance(event):
                event.attend(name, person)
                print('Attends.')
                person.events_attended += 1
            else:
                person.home_alone()
                print('Stays home.')
        event.occur()

    print()
    for name, person in people.items():
        person.print_state()
        person.print_personality()
        print('{} attended {} events'.format(name, person.events_attended))
        print()


if __name__ == '__main__':
    main()
