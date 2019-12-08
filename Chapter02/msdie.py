import random

class MSDie:
    '''
    Multi-sided 
    
    Instance Variables:
        current_value
        num_sides
    '''

    def __init__(self, side):
        self.num_sides = side
        self.current_value = self.roll()

    def roll(self):
        # return random.randint(1, self.num_sides)
        self.current_value = random.randrange(1,self.num_sides+1)
        return self.current_value

    def __str__(self):
        return str(self.current_value)

    def __repr__(self):
        return f"MSDie({self.num_sides}) : {self.current_value}"


my_die = MSDie(6)
for i in range(5):
    my_die.roll()
    print(my_die)


# use array to show the representation of class MSDie
print([MSDie(5), MSDie(20)])
print(MSDie(5), MSDie(20))