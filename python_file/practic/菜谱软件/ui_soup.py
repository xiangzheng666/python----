# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uu.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets
import word_clod
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class MyFigure(FigureCanvas):
    def __init__(self):
        self.fig = Figure(figsize=(5, 2), dpi=100)
        super(MyFigure, self).__init__(self.fig)
        self.axes = self.fig.add_subplot(111)

    def plot(self,m):
        self.axes.clear()
        self.axes.imshow(m)
        plt.subplots_adjust(wspace=0.4, hspace=0.5)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(654, 515)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(70, 20, 151, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 20, 131, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(70, 60, 521, 181))
        self.textEdit.setObjectName("textEdit")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(70, 290, 521, 181))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.canves=MyFigure()
        self.canves.setParent(self.frame)


        def b2():
            self.textEdit.setText('无')
        self.pushButton_2.clicked.connect(b2)

        def b1():

            today,im=word_clod.m()
            one= today.iloc[0,0:]
            two = today.iloc[1, 0:]
            thr = today.iloc[2, 0:]
            one='名称：   '+str(one["name"])+'\n'+'材料：   '+str(one["all"])+'\n'+'综合评分：   '+str(one["score"])+'\n'+'做法网址：   '+str(one["http"])
            two = '名称：   ' + str(two["name"]) + '\n' + '材料：   ' + str(two["all"]) + '\n' + '综合评分：   ' + str(two["score"]) + '\n' + '做法网址：   ' + str(two["http"])
            thr='名称：   ' + str(thr["name"]) + '\n' + '材料：   ' + str(thr["all"]) + '\n' + '综合评分：   ' + str(thr["score"]) + '\n' + '做法网址：   ' + str(thr["http"])
            stt=one+'\n\n\n'+two+'\n\n\n'+thr
            self.textEdit.setText(stt)

            self.canves.close_event()
            self.canves.plot(im)
            self.canves.draw()
        self.pushButton.clicked.connect(b1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "菜单生成"))
        self.pushButton_2.setText(_translate("Form", "清除"))

from PyQt5.Qt import QApplication,QWidget
import sys

if __name__ == '__main__':

    app=QApplication(sys.argv)

    w=QWidget()
    m=Ui_Form()
    m.setupUi(w)

    w.show()
    app.exec()