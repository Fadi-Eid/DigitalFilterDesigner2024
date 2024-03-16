from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import FIR_LeastSquares as FIR
import resources


class Ui_Form(object):
    def setupUi(self, Form):
        
        self.filter = None
        Form.setObjectName("Digital Filter Designer")
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
        self.horizontalLayout.setContentsMargins(50, 20, 50, 20)
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.spinBox = QtWidgets.QSpinBox(Form)
        self.spinBox.setMinimumSize(QtCore.QSize(80, 0))
        self.spinBox.setMaximumSize(QtCore.QSize(150, 16777215))
        self.spinBox.setMaximum(50000)
        self.spinBox.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.spinBox.setProperty("value", 501)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.valueChanged.connect(self.restart_filter)
        self.spinBox.setToolTip("Filter length")
        
        self.AddBandButton = QtWidgets.QPushButton(Form)
        self.AddBandButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.AddBandButton.setObjectName("AddBandButton")
        self.AddBandButton.clicked.connect(self.add_band)
        self.AddBandButton.setIcon(QtGui.QIcon(":/icons/Add.png"))
        
        self.horizontalLayout.addWidget(self.AddBandButton)
        self.horizontalLayout.addWidget(self.spinBox)
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
        self.ClearAllButton.setIcon((QtGui.QIcon(":/icons/Clear.png")))
        self.horizontalLayout_2.addWidget(self.ClearAllButton)
        self.DeleteLastButton = QtWidgets.QPushButton(Form)
        self.DeleteLastButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.DeleteLastButton.setObjectName("DeleteLastButton")
        self.DeleteLastButton.clicked.connect(self.delete_last_clicked)
        self.DeleteLastButton.setIcon((QtGui.QIcon(":/icons/Delete.png")))
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
        self.SaveButton.setIcon((QtGui.QIcon(":/icons/Save.png")))
        self.SaveButton.clicked.connect(self.save_coeffs)
        self.horizontalLayout_3.addWidget(self.SaveButton, 0, QtCore.Qt.AlignVCenter)
        self.PlotButton = QtWidgets.QPushButton(Form)
        self.PlotButton.setObjectName("PlotButton")
        self.PlotButton.clicked.connect(self.plot_clicked)
        self.PlotButton.setIcon((QtGui.QIcon(":/icons/Plot.png")))
        self.horizontalLayout_3.addWidget(self.PlotButton, 0, QtCore.Qt.AlignVCenter)
        self.CheckButton = QtWidgets.QPushButton(Form)
        self.CheckButton.setObjectName("CheckButton")
        self.CheckButton.clicked.connect(self.check_clicked)
        self.CheckButton.setIcon((QtGui.QIcon(":/icons/Check.png")))
        self.horizontalLayout_3.addWidget(self.CheckButton, 0, QtCore.Qt.AlignVCenter)
        self.CodeButton = QtWidgets.QPushButton(Form)
        self.CodeButton.setObjectName("CodeButton")
        self.CodeButton.setIcon((QtGui.QIcon(":/icons/Code.png")))
        self.CodeButton.clicked.connect(self.generateCode)
        self.horizontalLayout_3.addWidget(self.CodeButton, 0, QtCore.Qt.AlignVCenter)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.setStretch(2, 6)
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
        self.verticalLayout_5.setStretch(2, 1)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.filter_created = 0
        self.filter = None
        self.bands_list = []
        self.add_band_info()
        self.add_band()
        self.plot_on_canvas()

    def restart_filter(self):
        self.filter_created = 0
        self.filter = None

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", " "))
        Form.setWindowIcon((QtGui.QIcon(":/icons/icon.png")))
        
        self.TitleLabel.setText(_translate("Form", "Digital Filter Designer - 2024"))
        self.AddBandButton.setText(_translate("Form", " Add Band"))
        self.ClearAllButton.setText(_translate("Form", " Clear All"))
        self.DeleteLastButton.setText(_translate("Form", " Delete Last"))
        self.SaveButton.setText(_translate("Form", " Save"))
        self.PlotButton.setText(_translate("Form", " Plot"))
        self.CheckButton.setText(_translate("Form", " Check"))
        self.CodeButton.setText(_translate("Form", " Code"))
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
        self.filter_created = 0
        self.filter = None
        self.plot_on_canvas()

    def add_band(self):
        if len(self.bands_list) >= 8:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle(" ")
            msg.setText("Maximum number of Bands is 8      ")
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.exec_()
            return
        edit1 = QtWidgets.QLineEdit(Form)
        edit1.setFont(QtGui.QFont("Century Gothic"))
        edit1.textChanged.connect(self.plot_on_canvas)
        edit2 = QtWidgets.QLineEdit(Form)
        edit2.textChanged.connect(self.plot_on_canvas)
        edit3 = QtWidgets.QLineEdit(Form)
        edit3.textChanged.connect(self.plot_on_canvas)
        edit4 = QtWidgets.QLineEdit(Form)
        edit4.textChanged.connect(self.restart_filter)
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
            self.filter_created = 0
            self.filter = None
            

    def delete_last_clicked(self):
        if len(self.bands_list) >= 2:
            band = self.bands_list.pop()
            self.formLayout.removeRow(band)
            self.plot_on_canvas()
            self.filter_created = 0
            self.filter = None

    def is_valid_float(self, val):
        try:
            float(val)
            return True
        except ValueError:
            return False

    def create_filter(self):
        if self.filter_created == 1:
            return 1    # filter already created
        if len(self.bands_list) >= 2:
            weights = []
            numtaps = self.spinBox.value()
            bands = []
            desired = []
            
            iter = 0
            for edit in self.bands_list:
                iter += 1
                lower = edit.itemAt(0).widget().text()
                upper = edit.itemAt(1).widget().text()
                gain = edit.itemAt(2).widget().text()
                weight = edit.itemAt(3).widget().text()

                if self.is_valid_float(lower) and self.is_valid_float(upper) and self.is_valid_float(gain) and self.is_valid_float(weight):
                    lower = float(lower)
                    upper = float(upper)
                    gain = float(gain)
                    weight = float(weight)

                    if weight < 1 or weight > 10:
                        msg = QtWidgets.QMessageBox()
                        msg.setWindowTitle("Error ")
                        msg.setText(f"Weight of band {iter} must be between 1 and 10    ")
                        msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                        msg.exec_()
                        self.filter_created = 0
                        self.filter = None
                        return 4

                    if lower >= upper:
                        self.filter_created = 0
                        msg = QtWidgets.QMessageBox()
                        msg.setWindowTitle("Error ")
                        msg.setText(f"Band edges in band {iter} are not in ascending order    ")
                        msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                        msg.exec_()
                        self.filter = None
                        return 0    # not good -> band edges are not in ascending order or transition is zero
                    else:
                        bands.append(lower)
                        bands.append(upper)
                        desired.append(gain)
                        desired.append(gain)
                        weights.append(weight)
                else:
                    self.filter_created = 0
                    self.filter = None
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle("Error ")
                    msg.setText("Non-numerical or empty input")
                    msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    msg.exec_()
                    return 2 # non-digits input
        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Error ")
            msg.setText("Minimum number of bands is 2")
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.exec_()
            self.filter_created = 0
            self.filter = None
            return 1    # minimum is two bands
        
        fs = bands[-1] * 2
        bands[0] = 0.0

        # check if the order is ascending
        isAscending = True
        for i in range(len(bands) - 1):
            if bands[i] > bands[i+1]:
                isAscending = False
                break
        if isAscending == False:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Error ")
            msg.setText("Band edges are not in ascending order")
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.exec_()
            self.filter_created = 0
            self.filter = None
            return 3
        
        self.filter = FIR.FIR_Filter(fs, numtaps, bands, desired, weights)
        self.filter_created = 1
        return 1


    def check_clicked(self):
        # validate all inputs
        self.enable_buttons(False)
        if self.filter_created == 0:
            self.create_filter()
        if self.filter_created == 0:
            self.enable_buttons(True)
            self.DelayLabel.setText("Delay:")
            self.AvgHealthLabel.setText("Health: ")
            return 5
        delay = self.filter.Delay()
        health = self.filter.HealthScore()
        if delay >= 1000:
            self.DelayLabel.setText("Delay: " + str(delay/1000) + "s")
        else: 
            self.DelayLabel.setText("Delay: " + str(delay) + "ms")
        self.AvgHealthLabel.setText("Health: " + health)
        if health == "Best":
            self.AvgHealthLabel.setStyleSheet("background-color : green")
        elif health == "Good":
            self.AvgHealthLabel.setStyleSheet("background-color : lightgreen")
        elif health == "Average":
            self.AvgHealthLabel.setStyleSheet("background-color : yellow")
        elif health == "Below Average":
            self.AvgHealthLabel.setStyleSheet("background-color : orange")
        else:
            self.AvgHealthLabel.setStyleSheet("background-color : red")

        

        self.enable_buttons(True)


    def save_coeffs(self):
        self.enable_buttons(False)
        if self.filter_created == 0:
            self.create_filter()
        if self.filter_created == 0:
            self.enable_buttons(True)
            return 5
        folder_dialog = QtWidgets.QFileDialog()
        folder = folder_dialog.getExistingDirectory()
        if folder == "":
            self.enable_buttons(True)
            return 6
        self.filter.SaveCoeffs(folder)
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Success ")
        msg.setText("Coefficients saved: coefficients.csv")
        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Close)
        msg.exec_()

        self.enable_buttons(True)


    def plot_on_canvas(self):
        self.DelayLabel.setText("Delay: ")
        self.AvgHealthLabel.setText("Health: ")
        self.AvgHealthLabel.setStyleSheet("background-color: ")
        self.filter_created = 0
        self.filter = None
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
                    try:
                        lower = float(lower)
                    except ValueError:
                        self.figure.clear()
                        return
                    try:
                        upper = float(upper)
                    except ValueError:
                        self.figure.clear()
                        return
                    try:
                        gain = float(gain)
                    except ValueError:
                        pass
                    if lower < upper:
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
            plt.title("Expected Response", fontsize=11)
            plt.style.use('ggplot')
            # refresh canvas
            self.canvas.draw()

    def enable_buttons(self, en):
        #self.PlotButton.setEnabled(en)
        self.CheckButton.setEnabled(en)
        self.CodeButton.setEnabled(en)
        self.DeleteLastButton.setEnabled(en)
        self.ClearAllButton.setEnabled(en)
        self.AddBandButton.setEnabled(en)
        self.SaveButton.setEnabled(en)
        self.PlotButton.setEnabled(en)
        QtWidgets.QApplication.processEvents()


    def plot_clicked(self):
        # disable buttons
        self.enable_buttons(False)

        if self.filter_created == 0:
            self.create_filter()

        if self.filter_created == 0:
            self.enable_buttons(True)
            
            return 1    # problem with inputs
        
        else:
            self.filter.PlotAmplitudeLinear()
            self.filter.PlotAmplitudeLogarithmic()
            self.filter.PlotImpulse()
            self.enable_buttons(True)
            return
        
    def generateCode(self):
        self.enable_buttons(False)
        if self.filter_created == 0:
            self.create_filter()
        if self.filter_created == 0:
            self.enable_buttons(True)
            return 5
        
        folder_dialog = QtWidgets.QFileDialog()
        folder = folder_dialog.getExistingDirectory()

        if folder == "":
            self.enable_buttons(True)
            return 6     
           
        self.filter.GenerateCode(folder)

        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Success ")
        msg.setText("MATLAB code generated: filter.m")
        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Close)
        msg.exec_()

        self.enable_buttons(True)
        
        return




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

