from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QVBoxLayout
from random import *
app=QApplication([])
main_win=QWidget()
main_win.setWindowTitle("Определитель победителя")
button=QPushButton("Сгенерировать")
text=QLabel("Нажми, чтобы узнать победителя")
winner=QLabel("?")
line= QVBoxLayout()
line.addWidget(text,alignment=Qt.AlignCenter)
line.addWidget(winner,alignment=Qt.AlignCenter)
line.addWidget(button,alignment=Qt.AlignCenter)
main_win.setLayout(line)
def show_winner():
    numb=randint(0,99)
    winner.setText(str(numb))
button.clicked.connect(show_winner)
main_win.show()
app.exec_()