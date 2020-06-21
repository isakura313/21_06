""" Простое приветствие на PyQt"""
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget #представляет из себя одно окно

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Первая программа на PyQt5")
window.setGeometry(400, 400, 600, 600)
"""параметры x и y - положение окна в экрана два первых аргумента
    следующие два ширина и высота приложения
"""
helloMSG = QLabel("<h1> Привет</h1>", parent=window)
helloMSG.move(260, 15)
hello2 = QLabel("<h2>OZON </h2>", parent=window)
hello2.move(260, 55)
# hello2.mov

window.show()
sys.exit(app.exec())

