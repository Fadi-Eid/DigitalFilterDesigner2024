# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_gui_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


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
        self.horizontalLayout.addWidget(self.AddBandButton)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label, 0, QtCore.Qt.AlignRight)
        self.spinBox = QtWidgets.QSpinBox(Form)
        self.spinBox.setMinimumSize(QtCore.QSize(80, 0))
        self.spinBox.setMaximumSize(QtCore.QSize(150, 16777215))
        self.spinBox.setMaximum(50000)
        self.spinBox.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.spinBox.setProperty("value", 501)
        self.spinBox.setObjectName("spinBox")
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
        self.horizontalLayout_2.addWidget(self.ClearAllButton)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
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
        self.horizontalLayout_3.addWidget(self.CheckButton, 0, QtCore.Qt.AlignVCenter)
        self.CodeButton = QtWidgets.QPushButton(Form)
        self.CodeButton.setObjectName("CodeButton")
        self.horizontalLayout_3.addWidget(self.CodeButton, 0, QtCore.Qt.AlignVCenter)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.setStretch(0, 6)
        self.verticalLayout_2.setStretch(1, 1)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4.setStretch(0, 1)
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

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.TitleLabel.setText(_translate("Form", "Digital Filter Designer - 2024"))
        self.AddBandButton.setText(_translate("Form", "Add Band"))
        self.label.setText(_translate("Form", "Length"))
        self.ClearAllButton.setText(_translate("Form", "Clear All"))
        self.pushButton.setText(_translate("Form", "Delete Last"))
        self.SaveButton.setText(_translate("Form", "Save"))
        self.PlotButton.setText(_translate("Form", "Plot"))
        self.CheckButton.setText(_translate("Form", "Check"))
        self.CodeButton.setText(_translate("Form", "Code"))
        self.DelayLabel.setText(_translate("Form", "Delay: "))
        self.AvgHealthLabel.setText(_translate("Form", "Avg. Health:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
