import sys
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QWidget, QLineEdit, QFormLayout
from PyQt6.QtWidgets import QPushButton, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import QSize


class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
 
        self.setMinimumSize(QSize(300, 400))
        self.setWindowTitle("Add bands test code")

        self.controls = []

        button1 = QPushButton('add band', self)
        button1.clicked.connect(self.add_band_clicked)
        button2 = QPushButton('remove band', self)
        button2.clicked.connect(self.remove_band_clicked)
        button3 = QPushButton('submit', self)
        button3.clicked.connect(self.submit_clicked)

        vbox = QVBoxLayout()
        formlayout = QFormLayout()
        vbox.addLayout(formlayout)
        hbox = QHBoxLayout()
        hbox.addWidget(button1)
        hbox.addWidget(button2)
        vbox.addLayout(hbox)
        vbox.addWidget(button3)
        self.setLayout(vbox)
        self.formlayout = formlayout

        self.count = 0
        self.add_band_clicked()

    def add_band_clicked(self):
        if self.count == 0:
            edit = QLineEdit(self)
            edit.setVisible(False)
            self.controls.append(edit)
            self.formlayout.addRow(f' ', edit)
            self.count += 1
            return
        
        if self.count == 1:
            edit = self.controls.pop()
            self.formlayout.removeRow(edit)
            edit = None
            edit1 = QLineEdit(self)
            edit1.setVisible(True)
            edit2 = QLineEdit(self)
            edit2.setVisible(True)
            edit = QHBoxLayout()
            edit.addWidget(edit1)
            edit.addWidget(edit2)
            self.controls.append(edit)
            self.formlayout.addRow(f'Band {self.count}', edit)
            self.count += 1
            return

        if self.count > 6:
            return
        
        edit1 = QLineEdit(self)
        edit1.setVisible(True)
        edit2 = QLineEdit(self)
        edit2.setVisible(True)
        edit = QHBoxLayout()
        edit.addWidget(edit1)
        edit.addWidget(edit2)
        self.controls.append(edit)
        self.formlayout.addRow(f'Band {self.count}', edit)
        self.count += 1

    def remove_band_clicked(self):
        if len(self.controls) > 1:
            edit = self.controls.pop()
            self.formlayout.removeRow(edit)
            self.count -= 1
            return
        else:
            edit = self.controls.pop()
            self.formlayout.removeRow(edit)
            edit = None
            edit = QLineEdit(self)
            edit.setVisible(False)
            self.controls.append(edit)
            self.formlayout.addRow(' ', edit)
            self.count = 1

    def submit_clicked(self):
        if (self.count-1) > 0:
            for edit in self.controls:
                edit1 = edit.itemAt(0).widget()
                edit2 = edit.itemAt(1).widget()
                if edit1.text() != "" and edit1.text() != "":
                    print(edit1.text())
                    print(edit2.text())
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec())