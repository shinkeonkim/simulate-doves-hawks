import sys
from game import Game
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 1200, 700)
        
        self.setWindowTitle("Doves & Hawks")
        self.container = QHBoxLayout()
        self.setLayout(self.container)
        

        self.input_container = QVBoxLayout()

        self.foods = QHBoxLayout()
        self.doves = QHBoxLayout()
        self.hawks = QHBoxLayout()
        self.turn = QHBoxLayout()

        self.foods_label = QLabel("foods: ")
        self.doves_label = QLabel("doves: ")
        self.hawks_label = QLabel("hawks: ")
        self.turn_label = QLabel("turn: ")

        self.foods_cnt = QLineEdit("40")
        self.doves_cnt = QLineEdit("1")
        self.hawks_cnt = QLineEdit("1")
        self.turn_edit = QLineEdit("20")

        self.foods.addWidget(self.foods_label)
        self.foods.addWidget(self.foods_cnt)
        self.doves.addWidget(self.doves_label)
        self.doves.addWidget(self.doves_cnt)
        self.hawks.addWidget(self.hawks_label)
        self.hawks.addWidget(self.hawks_cnt)
        self.turn.addWidget(self.turn_label)
        self.turn.addWidget(self.turn_edit)

        self.input_container.addLayout(self.foods)
        self.input_container.addLayout(self.doves)
        self.input_container.addLayout(self.hawks)
        self.input_container.addLayout(self.turn)
        

        self.container.addLayout(self.input_container)

        self.pushButton = QPushButton("simulate")
        self.pushButton.clicked.connect(self.pushButtonClicked)
        self.input_container.addWidget(self.pushButton)
        

    def pushButtonClicked(self):
        self.count = {
            'foods' : int(self.foods_cnt.text()),
            'doves' : int(self.doves_cnt.text()),
            'hawks' : int(self.hawks_cnt.text()),
        }

        self.percentage = {
            'doves' : {
                'doves' : 1,
                'hawks' : 1/2,
            },
            'hawks' : {
                'doves': 3/2,
                'hawks': 1/2,
            }
        }

        game = Game(self.count, self.percentage)

        turn = int(self.turn_edit.text())
        result = game.simulate(turn)
        print(result)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = Window()
    mywindow.show()
    app.exec_()