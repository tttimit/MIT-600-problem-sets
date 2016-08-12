# what is the probability of rolling five 6-sides dice, and having
# them all display the same number? write a simulation to solve it.
import random
class dice():
    def __init__(self):
        self.point = random.randrange(1, 7)

    def get_point(self):
        return self.point

    def roll(self):
        self.point = random.randrange(1, 7)
##
## TEST DICE
##        
def test_dict(num_trials):
    f = dice()
    dic = {}
    for i in range(num_trials):
        f.roll()
        if f.get_point() in dic:
            dic[f.get_point()] += 1
        else:
            dic[f.get_point()] = 1
    result = {}
    for i in dic:
        result[i] = float(dic[i]) / num_trials
    print("prosibalities for every side:", result)
##
##test_dict(1000000)
##

class game():
    def __init__(self):
        self.dices = []
        for i in range(6):
            self.dices.append(dice())

    def one_shot(self):
        for i in self.dices:
            i.roll()

    def get_result(self):
        result = []
        for i in self.dices:
            result.append(i.get_point())
        return result

    def is_same(self):
        r = self.get_result()
        if sum(r) == 6 * r[0]:
            return True
        else:
            return False

def simulation(number_trials):
    good_shot = 0
    g = game()
    for i in range(number_trials):
        g.one_shot()
        if g.is_same():
            good_shot += 1
    print("prob is:", float(good_shot) / number_trials)
    print("1/36 is:", 1.0 / 36)

simulation(10000000)
    

            
            
    
