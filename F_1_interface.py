import sys
from PyQt5.QtCore import center, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
import numpy as np

class Fenetre(QWidget):
    def __init__(self, _matrix):
        QWidget.__init__(self)

        matrix = _matrix
        # création de l'étiquette
        self.label = QLabel(str(matrix))
        self.label.setStyleSheet("font : 18pt")
        self.label.setAlignment(Qt.AlignCenter)
        # mise en place du gestionnaire de mise en forme
        self.label2 = QLabel("Matrice")
        self.label2.setStyleSheet("font : 18pt")
        self.label2.setAlignment(Qt.AlignCenter)
        layout = QVBoxLayout()

        layout.addWidget(self.label2)
        layout.addWidget(self.label)
        
        self.setLayout(layout)
        
        self.setWindowTitle("Matrice")

class Fenetre2(QWidget):
    def __init__(self, _matrix):
        QWidget.__init__(self)

        matrix = _matrix
        # création de l'étiquette
        self.label = QLabel(str(matrix))
        self.label.setStyleSheet("font : 18pt")
        self.label.setAlignment(Qt.AlignCenter)
        # mise en place du gestionnaire de mise en forme
        self.label2 = QLabel("Matrice des plus courts chemins")
        self.label2.setStyleSheet("font : 18pt")
        self.label2.setAlignment(Qt.AlignCenter)
        layout = QVBoxLayout()

        layout.addWidget(self.label2)
        layout.addWidget(self.label)
        
        self.setLayout(layout)
        
        self.setWindowTitle("Matrice des plus courts chemins")




def interface(matrix):
    app = QApplication.instance() 
    if not app:
        app = QApplication(sys.argv)
        
    fen = Fenetre(matrix)
    fen.resize(600,400)
    fen.show()

    app.exec_()

def interface2(matrix):
    app = QApplication.instance() 
    if not app:
        app = QApplication(sys.argv)
        
    fen = Fenetre2(matrix)
    fen.resize(600,400)
    fen.show()

    app.exec_()