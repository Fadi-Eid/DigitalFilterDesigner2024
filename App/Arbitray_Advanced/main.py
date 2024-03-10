from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(898, 575)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.TitleLabel = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        self.TitleLabel.setFont(font)
        self.TitleLabel.setObjectName("TitleLabel")
        self.verticalLayout_5.addWidget(self.TitleLabel, 0, QtCore.Qt.AlignTop)
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_5.addWidget(self.line_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(50, -1, 50, -1)
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.AddBandButton = QtWidgets.QPushButton(Form)
        self.AddBandButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.AddBandButton.setObjectName("AddBandButton")
        self.AddBandButton.clicked.connect(self.add_band)
        self.horizontalLayout.addWidget(self.AddBandButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(50, -1, 50, -1)
        self.horizontalLayout_2.setSpacing(30)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ClearAllButton = QtWidgets.QPushButton(Form)
        self.ClearAllButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.ClearAllButton.setObjectName("ClearAllButton")
        self.ClearAllButton.clicked.connect(self.clear_all_clicked)
        self.horizontalLayout_2.addWidget(self.ClearAllButton)
        self.DeleteLastButton = QtWidgets.QPushButton(Form)
        self.DeleteLastButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.DeleteLastButton.setObjectName("DeleteLastButton")
        self.DeleteLastButton.clicked.connect(self.delete_last_clicked)
        self.horizontalLayout_2.addWidget(self.DeleteLastButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 5)
        self.verticalLayout.setStretch(2, 1)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_4.addWidget(self.line_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        # create a horizontal layout
        self.hbox = QtWidgets.QHBoxLayout(self.frame)
        self.hbox.setObjectName("hbox")
        # Canvas Here
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        # End of canvas
        # Add canvas
        self.hbox.addWidget(self.canvas)
        ## end of hbox layout

        self.verticalLayout_2.addWidget(self.frame)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(5, -1, 5, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.SaveButton = QtWidgets.QPushButton(Form)
        self.SaveButton.setObjectName("SaveButton")
        self.horizontalLayout_3.addWidget(self.SaveButton, 0, QtCore.Qt.AlignVCenter)
        self.PlotButton = QtWidgets.QPushButton(Form)
        self.PlotButton.setObjectName("PlotButton")
        self.horizontalLayout_3.addWidget(self.PlotButton, 0, QtCore.Qt.AlignVCenter)
        self.CheckButton = QtWidgets.QPushButton(Form)
        self.CheckButton.setObjectName("CheckButton")
        self.CheckButton.clicked.connect(self.parse_edits)
        self.horizontalLayout_3.addWidget(self.CheckButton, 0, QtCore.Qt.AlignVCenter)
        self.CodeButton = QtWidgets.QPushButton(Form)
        self.CodeButton.setObjectName("CodeButton")
        self.horizontalLayout_3.addWidget(self.CodeButton, 0, QtCore.Qt.AlignVCenter)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.setStretch(0, 6)
        self.verticalLayout_2.setStretch(1, 1)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4.setStretch(1, 2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_5.addWidget(self.line)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.DelayLabel = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.DelayLabel.setFont(font)
        self.DelayLabel.setObjectName("DelayLabel")
        self.horizontalLayout_5.addWidget(self.DelayLabel)
        self.AvgHealthLabel = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.AvgHealthLabel.setFont(font)
        self.AvgHealthLabel.setObjectName("AvgHealthLabel")
        self.horizontalLayout_5.addWidget(self.AvgHealthLabel)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.verticalLayout_5.setStretch(2, 5)
        self.verticalLayout_5.setStretch(3, 1)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.bands_list = []
        self.add_band_info()
        self.add_band()
        self.plot_on_canvas()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.TitleLabel.setText(_translate("Form", "Digital Filter Designer - 2024"))
        self.AddBandButton.setText(_translate("Form", "Add Band"))
        self.ClearAllButton.setText(_translate("Form", "Clear All"))
        self.DeleteLastButton.setText(_translate("Form", "Delete Last"))
        self.SaveButton.setText(_translate("Form", "Save"))
        self.PlotButton.setText(_translate("Form", "Plot"))
        self.CheckButton.setText(_translate("Form", "Check"))
        self.CodeButton.setText(_translate("Form", "Code"))
        self.DelayLabel.setText(_translate("Form", "Delay: "))
        self.AvgHealthLabel.setText(_translate("Form", "Avg. Health:"))

    def add_band_info(self):
        label1 = QtWidgets.QLabel("Lower Edge")
        label1.setFont(QtGui.QFont("Century Gothic"))
        label2 = QtWidgets.QLabel("Upper Edge")
        label2.setFont(QtGui.QFont("Century Gothic"))
        label3 = QtWidgets.QLabel("Gain")
        label3.setFont(QtGui.QFont("Century Gothic"))
        label4 = QtWidgets.QLabel("Weight")
        label4.setFont(QtGui.QFont("Century Gothic"))
        label = QtWidgets.QHBoxLayout()
        label.addWidget(label1, 0, QtCore.Qt.AlignHCenter)
        label.addWidget(label2, 0,  QtCore.Qt.AlignHCenter)
        label.addWidget(label3, 0, QtCore.Qt.AlignHCenter)
        label.addWidget(label4, 0, QtCore.Qt.AlignHCenter)
        self.formLayout.addRow('Band #', label)

    def add_band(self):
        if len(self.bands_list) >= 8:
            return
        edit1 = QtWidgets.QLineEdit(Form)
        edit1.setFont(QtGui.QFont("Century Gothic"))
        edit1.textChanged.connect(self.plot_on_canvas)
        edit2 = QtWidgets.QLineEdit(Form)
        edit2.textChanged.connect(self.plot_on_canvas)
        edit3 = QtWidgets.QLineEdit(Form)
        edit3.textChanged.connect(self.plot_on_canvas)
        edit4 = QtWidgets.QLineEdit(Form)
        edit = QtWidgets.QHBoxLayout()
        edit.addWidget(edit1)
        edit.addWidget(edit2)
        edit.addWidget(edit3)
        edit.addWidget(edit4)
        self.bands_list.append(edit)
        self.formLayout.addRow(f'Band {len(self.bands_list)}', edit)

    def clear_all_clicked(self):
        if len(self.bands_list) >= 1:
            for band in self.bands_list:
                edit1 = band.itemAt(0).widget()
                edit2 = band.itemAt(1).widget()
                edit3 = band.itemAt(2).widget()
                edit4 = band.itemAt(3).widget()
                edit1.setText("")
                edit2.setText("")
                edit3.setText("")
                edit4.setText("")
            self.plot_on_canvas()
            

    def delete_last_clicked(self):
        if len(self.bands_list) >= 2:
            band = self.bands_list.pop()
            self.formLayout.removeRow(band)
            self.plot_on_canvas()

    def parse_edits(self):
        if len(self.bands_list) >= 1:
            for edit in self.bands_list:
                edit1 = edit.itemAt(0).widget()
                edit2 = edit.itemAt(1).widget()
                edit3 = edit.itemAt(2).widget()
                edit4 = edit.itemAt(3).widget()
                if edit1.text() != "" and edit2.text() != "":
                    if edit3.text() != "" and edit4.text() != "":
                        print(edit1.text() + " " + edit2.text() + " " + edit3.text() + " " + edit4.text())

    def plot_on_canvas(self):
        # clear the canvas
        self.figure.clear()
        num_bands = len(self.bands_list)
        x = []
        y = []
        if num_bands >= 1:
            for edit in self.bands_list:
                lower = edit.itemAt(0).widget().text() # low edge
                upper = edit.itemAt(1).widget().text() # upp edge
                gain = edit.itemAt(2).widget().text() # gain
                if lower != "" and upper != "" and gain != "":
                    if lower < upper:
                        try:
                            lower = float(lower)
                        except ValueError:
                            print("Could not convert the string to a float")
                        try:
                            upper = float(upper)
                        except ValueError:
                            print("Could not convert the string to a float")
                        try:
                            gain = float(gain)
                        except ValueError:
                            print("Could not convert the string to a float")
                        x.append(lower)
                        x.append(upper)
                        y.append(gain)
                        y.append(gain)

        # check if the order is ascending
        isAscending = True
        for i in range(len(x) - 1):
            if x[i] > x[i+1]:
                isAscending = False
                break
        if isAscending == True:
            plt.plot(x, y)
            # refresh canvas
            self.canvas.draw()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
