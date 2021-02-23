import numpy as np

class Item:
    def __init__(self, itemcost = 100, currentSF = 0, desiredSF = 15):
        self.itemcost = itemcost
        self.currentSF = currentSF
        self.desiredSF = desiredSF
        self.numoffail = 0

        self.upgcost =  [
                            0,      0,      0,      0,      0,      0,
                            0,      0,      0,      0,      0,      0,
                            0.6,    1.3,    1.4,    2.1,    2.1,    2.1,
                            2.8,    2.8,    7,7,    19.4,   29.4,   39.6
                        ]
        self.odds =     [
                            95,     90,     85,     85,     80,     75,
                            70,     65,     60,     55,     50,     45,
                            40,     35,     30,     30,     30,     30,
                            30,     30,     30,     30,     3,      2,
                        ]
        self.boom =     [
                            0,      0,      0,      0,      0,      0,
                            0,      0,      0,      0,      0,      0,
                            0.6,    1.3,    1.4,    2.1,    2.1,    2.1,
                            2.8,    2.8,    7,7,    19.4,   29.4,   39.6
                        ]

        self.totalcost = self.itemcost



    def run(self):
        if(self.checkincrease() == True):
           pass
        elif(self.checkdestroyed() == True):
            pass
        else:
            if self.currentSF < 6:
                pass
            else:
                if self.currentSF % 5 == 0:
                    pass
                else:
                    self.currentSF -= 1
                    self.numoffail += 1
        if(self.currentSF != self.desiredSF):
            self.run()
        return self.totalcost

    def checkincrease(self):
        if np.random.randint(1,101) <= self.odds[self.currentSF]:
            self.totalcost += self.upgcost[self.currentSF]  # List of costs
            self.currentSF += 1
            return True
        return False

    def checkdestroyed(self):
        if np.random.randint(1, 101) <= self.boom[self.currentSF]:
            self.totalcost += self.itemcost + self.upgcost[self.currentSF]  # List of costs
            self.currentSF = 0
            self.numoffail = 0
            return True
        return False

def getuserinput():
    itemcost = int(input('Item cost in million mesos: '))
    currentSF = int(input('Current Starforce: '))
    desiredSF = int(input('Desired Starforce: '))

    cost = []
    for i in range(100):
        obj = Item(itemcost, currentSF, desiredSF)
        cost.append(obj.run())
    avgcost = np.mean(cost)
    print(f"Average cost after 100 simulations is {avgcost}")



if __name__ == '__main__':
    getuserinput()


