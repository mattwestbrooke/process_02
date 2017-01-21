# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'data_viewer_005_UI.ui'
#
# Created: Wed Dec 14 12:05:23 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Dv_005(QtGui.QWidget):
    def __init__(self):
        super(Dv_005, self).__init__()

        self.setupUi()
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        self.id = id
        self.variables = []

    def set_variable(self, attribute, value):
        found = False
        for ii in self.variables:
            if ii[0] == attribute:
                ii[1] = value
                found = True
        if found == False:
            self.variables.append([attribute, value])
        self.populate_list()
        self.tableWidget.resizeColumnsToContents()
        return found

    def get_variable(self, attribute):
        found = False
        result = ""
        for jj in self.variables:
            if jj[0] == attribute:
                result = jj[1]
                found = True
        self.populate_list()
        return result, found

    def populate_list(self):
        #print "populating keys"
        self.tableWidget.setRowCount(0)
        for ll in self.variables:
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(rowPosition, 0, QtGui.QTableWidgetItem(ll[0]))
            self.tableWidget.setItem(rowPosition, 1, QtGui.QTableWidgetItem(ll[1]))
        self.tableWidget.resizeColumnsToContents()

    def setupUi(self):
        self.setObjectName("Frame")
        self.resize(565, 90)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.setFont(font)

        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtGui.QTableWidget()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setFrameShadow(QtGui.QFrame.Plain)
        self.tableWidget.setLineWidth(0)
        self.tableWidget.setAutoScrollMargin(5)
        self.tableWidget.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(300)
        self.gridLayout.addWidget(self.tableWidget, 0, 1, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setFrameShape(QtGui.QFrame.Box)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.setLayout(self.verticalLayout_2)
        self.show()

    def retranslateUi(self):
        self.setWindowTitle(QtGui.QApplication.translate("Frame", "Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("Frame", "NAME", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("Frame", "VALUE", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Frame", "0", None, QtGui.QApplication.UnicodeUTF8))

