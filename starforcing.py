import numpy as np
import PySimpleGUI as sg
import sys
import threading
import time


class Item:
    def __init__(self, itemlevel = 160, itemcost = 100, currentSF = 0, desiredSF = 15, starcatch = 1.00):
        self.itemlevel = itemlevel
        self.itemcost = itemcost * 1000000
        self.currentSF = currentSF
        self.desiredSF = desiredSF
        self.numoffail = 0
        self.starcatch = starcatch

        self.odds =     [
                            95,     90,     85,     80,     80,     75,
                            70,     65,     55,     50,     45,     35,
                            30,     30,     25,     25,     20,     15,
                            10,     10,     10,     10,     10,      10,
                            10
                        ]
        self.boom =     [
                            0,      0,      0,      0,      0,      0,
                            0,      0,      0,      0,      0,      0,
                            0.7,    1.5,    2.0,    2.4,    2.8,    3.5,
                            3.9,    4.6,    5.3,    6.0,    6.7,    7.5,
                            8.3
                        ]

        self.totalcost = 0


    def run(self):
        if(self.checkstatus() == True):
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

    def checkstatus(self):
        check = np.random.uniform(0, 100)
        if self.numoffail == 2 or check <= self.starcatch * self.odds[self.currentSF]:
            self.totalcost += self.upgradecost()
            self.currentSF += 1
            self.numoffail = 0
            return True
        elif check <= self.boom[self.currentSF] + self.starcatch * self.odds[self.currentSF]:
            self.totalcost += self.itemcost + self.upgradecost()  # List of costs
            self.currentSF = 0
            self.numoffail = 0

        return False

    def upgradecost(self):
        if self.currentSF < 10:
            return (1000 + (self.itemlevel**3)*(self.currentSF + 1)/25)
        elif self.currentSF < 15:
            return (1000 + ((self.itemlevel**3)*(self.currentSF + 1)**2.7)/400)
        elif self.currentSF < 18:
            return (1000 + ((self.itemlevel**3)*(self.currentSF + 1)**2.7)/120)
        elif self.currentSF < 20:
            return (1000 + ((self.itemlevel**3)*(self.currentSF + 1)**2.7)/110)
        else:
            return (1000 + ((self.itemlevel**3)*(self.currentSF + 1)**2.7)/100)


def getuserinput():
    sg.theme('Light Grey 6')
    layout = [
        [sg.Text('Item level', font=('Helvetica', 18), size=(25, 1)), sg.InputText()],
        [sg.Text('Item cost in million mesos', font=('Helvetica', 18), size=(25, 1)), sg.InputText()],
        [sg.Text('Current Star Force', font=('Helvetica', 18), size=(25, 1)), sg.InputText()],
        [sg.Text('Desired Star Force', font=('Helvetica', 18), size=(25, 1)), sg.InputText()],
        [sg.Checkbox('Enable Star Catching', font=('Helvetica', 18), enable_events=True, key='-STARCATCH')],
        [sg.Text(font=('Helvetica', 18), text_color='red', size=(40, 1), key='-OUTPUT-')],
        [sg.Submit()]
    ]
    window = sg.Window('Simple AriesMS Starforce Calculator', layout)
    starcatch = False

    while True:
        event, values = window.read()
        inputcheck = True
        try:
            itemlevel = int(values[0])
            itemcost = int(values[1])
            currentSF = int(values[2])
            desiredSF = int(values[3])
            starcatch = values['-STARCATCH']
        except:
            inputcheck = False
            window['-OUTPUT-'].update('Check if all input values are integers')

        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break

        if event.startswith('-STARCATCH'):
            starcatch = not starcatch
            window['-STARCATCH'].update(not starcatch)
        elif inputcheck == True:
            cost = []
            starmultiplier = 1.00
            if starcatch == True:
                starmultiplier = 1.04

            for i in range(100):
                obj = Item(itemlevel, itemcost, currentSF, desiredSF, starmultiplier)
                cost.append(obj.run())
            avgcost = round((np.mean(cost) / 1000000),2)

            window['-OUTPUT-'].update(f'Average cost over 100 simulations is: {avgcost:,}m' )
            time.sleep(1)



if __name__ == '__main__':
    sys.setrecursionlimit(1000000)
    threading.stack_size(200000000)
    thread = threading.Thread(target=getuserinput)
    thread.start()



