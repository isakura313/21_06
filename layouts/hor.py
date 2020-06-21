""" Простая верстка на PyQt"""
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget #представляет из себя одно окно
from PyQt5.QtWidgets import QPushButton #кнопочки, на которые можно нажимать
from PyQt5.QtWidgets import QLabel #кнопочки, на которые можно нажимать
from PyQt5.QtWidgets import QHBoxLayout #кнопочки, на которые можно нажимать


app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Первая программа на PyQt5")
window.setGeometry(400, 400, 600, 600)

layout = QHBoxLayout()  #создаем объект верстки

layout.addWidget(QPushButton("слева")) #добавляю сюда виджеты слева направо
layout.addWidget(QLabel("А я внезапно тут"))
layout.addWidget(QPushButton("по центру"))
layout.addWidget(QPushButton("справа"))

window.setLayout(layout)  #добавляю layout в Widget
window.show()
sys.exit(app.exec())

