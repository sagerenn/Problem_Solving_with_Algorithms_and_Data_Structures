
class Jug():

    def __init__(self, gallon):
        self.gallon = gallon
        self.contain = 0

    def to_jug(self, other_jug):
        other_jug.fill(self.contain)
        self.empty()
    
    def empty(self):
        self.contain = 0

    def full(self):
        self.contain = self.gallon

    def fill(self, add_gallon):
        self.contain += add_gallon
        if self.contain > self.gallon:
            self.contain = self.gallon

    def get_contain(self):
        return self.contain

    def get_gallon(self):
        return self.gallon


jug1, jug2, goal = 4, 3 ,2
temp_result = []

def fill_jug(state1, state2):
    if (state1, state2) == (goal, 0) or (state2, state1) == (goal, 0):
        print(state1, state2)
        return True

    if (state1, state2) in temp_result:
        return False
    else:
        temp_result.append( (state1, state2) )
        print(state1, state2)
        return ( fill_jug(0, state2) or \
                fill_jug(state1, 0) or \
                fill_jug(state1, jug2) or \
                fill_jug(jug1, state2) or \
                fill_jug(max(state1-jug2+state2, 0), min(jug2, state2+state1) ) or \
                fill_jug(min(jug1, state2+state1), max(state2-jug1+state1, 0) )
             )

fill_jug(0, 0)