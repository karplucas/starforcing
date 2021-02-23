import numpy as np
import PySimpleGUI as sg
import sys


class Item:
    def __init__(self, itemcost = 100, currentSF = 0, desiredSF = 15):
        self.itemcost = itemcost
        self.currentSF = currentSF
        self.desiredSF = desiredSF
        self.numoffail = 0

        self.upgcost =  [
                            0.01,       0,          0,          0.055,         0.1,          0.2,
                            0.3,        0.4,        0.5,        0.6,           5.470800,     6.919400,
                            8.588400,   10.490600,  2.638500,   30.087200,     35.437900,    41.351400,
                            47.850600,  54.958200,  62.696400,  71.087200,     80.152000,    89.912300,
                            100.389000
                        ]
        self.odds =     [
                            100,    95,     90,     85,     80,     75,
                            70,     65,     60,     55,     50,     45,
                            40,     35,     30,     30,     30,     30,
                            30,     30,     30,     30,     3,      2,
                            1
                        ]
        self.boom =     [
                            0,      0,      0,      0,      0,      0,
                            0,      0,      0,      0,      0,      0,
                            0,      0.6,    1.3,    1.4,    2.1,    2.1,
                            2.1,    2.8,    2.8,    7,7,    19.4,   29.4,
                            39.6
                        ]

        self.totalcost = 0



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
        if self.numoffail == 2 or np.random.randint(1,101) <= self.odds[self.currentSF]:
            self.totalcost += self.upgcost[self.currentSF]  # List of costs
            self.currentSF += 1
            self.numoffail = 0
            return True
        return False

    def checkdestroyed(self):
        if np.random.uniform(1, 100) <= self.boom[self.currentSF]:
            self.totalcost += self.itemcost + self.upgcost[self.currentSF]  # List of costs
            self.currentSF = 0
            self.numoffail = 0
            return True
        return False

def getuserinput():
    layout = [
        [sg.Text('Item cost in mesos (millions)', size=(25, 1)), sg.InputText()],
        [sg.Text('Current Star Force', size=(25, 1)), sg.InputText()],
        [sg.Text('Desired Star Force', size=(25, 1)), sg.InputText()],
        [sg.Text(size=(40, 1), key='-OUTPUT-')],
        [sg.Submit()]
    ]

    window = sg.Window('Simple AriesMS Starforce Calculator', layout)

    while True:

        event, values = window.read()


        itemcost = int(values[0])
        currentSF = int(values[1])
        desiredSF = int(values[2])

        cost = []
        for i in range(1000):
            obj = Item(itemcost, currentSF, desiredSF)
            cost.append(obj.run())
        avgcost = np.mean(cost)

        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break
        window['-OUTPUT-'].update('Average cost over 1000 simulations is: ' + str(avgcost))


if __name__ == '__main__':
    sys.setrecursionlimit(1000000)
    getuserinput()



