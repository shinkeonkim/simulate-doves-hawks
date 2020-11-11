import copy
from os import stat
import random

class Game:
    def __init__(self, count, percentage):
        self.count = {
            'foods' : count['foods'],
            'doves' : count['doves'],
            'hawks' : count['hawks'],
        }

        self.percentage = {
            'doves' : {
                'doves' : percentage['doves']['doves'],
                'hawks' : percentage['doves']['hawks'],
            },
            'hawks' : {
                'doves': percentage['hawks']['doves'],
                'hawks': percentage['hawks']['hawks'],
            }
        }


    def setCount(self, count):
        self.count = copy.deepcopy(count)
    

    def getCount(self):
        return self.count


    def simulate(self, turn = 100):
        ret = {}
        endTurn = turn
        for t in range(1, turn+1):
            if self.next():
                ret[t] = copy.deepcopy(self.count)
            else:
                endTurn = t-1
                break
        return {'ret': ret, 'endTurn' : endTurn}


    def next(self):
        if self.count['foods']*2 <= self.count['doves'] + self.count['hawks']:
            return False

        D = [[] for i in range(self.count['foods'])]
        
        for i in range(self.count['doves']):
            want = random.randint(0, self.count['foods'] - 1)
            while len(D[want]) >= 2:
                want = random.randint(0, self.count['foods'] - 1)
            D[want].append('doves')
                

        for i in range(self.count['hawks']):
            want = random.randint(0, self.count['foods'] - 1)
            while len(D[want]) >= 2:
                want = random.randint(0, self.count['foods'] - 1)
            D[want].append('hawks')

        for status in D:
            if len(status) == 0:
                continue
            elif len(status) == 1:
                self.count[status[0]] += 1
            else:
                for i in range(2):
                    p = self.percentage[status[i]][status[(i+1)%2]]
                    ret = self.eat(p)
                    if not ret[0]:
                        self.count[status[0]] -= 1
                    if ret[1]:
                        self.count[status[1]] += 1
        return True

    def eat(self, percentage):
        save_life = False
        new_life = False
        if percentage >= 1:
            save_life = True
            p = percentage - 1
            if random.random() <= p:
                new_life = True
        else:
            if random.random() <= percentage:
                save_life = True
        return [save_life, new_life]

    def __str__(self):
        return "foods: %d, doves: %d, hawks: %d" % (self.count['foods'],self.count['doves'],self.count['hawks'])

if __name__ == "__main__":
    count = {
        'foods' : 40,
        'doves' : 4,
        'hawks' : 1,
    }

    percentage = {
        'doves' : {
            'doves' : 1,
            'hawks' : 1/2,
        },
        'hawks' : {
            'doves': 3/2,
            'hawks': 1/2,
        }
    }

    game = Game(count, percentage)
    print("game1")
    print(game)
    game.next()
    print(game)

    game.next()
    print(game)
    game.next()
    print(game)
    print("-"*20)

    count = {
        'foods' : 100,
        'doves' : 10,
        'hawks' : 0,
    }

    percentage = {
        'doves' : {
            'doves' : 1,
            'hawks' : 1/2,
        },
        'hawks' : {
            'doves': 3/2,
            'hawks': 1/2,
        }
    }
    game2 = Game(count, percentage)
    result = game2.simulate(200)
    print(result)




