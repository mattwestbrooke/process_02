# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'key_filter_UI.ui'
#
# Created: Fri Dec 16 15:14:35 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import tree_functions
import sys
import os

ROOT_DIR = os.path.dirname(sys.modules['__main__'].__file__)

class filter_UI(QtGui.QWidget):
    update_filter_signal = QtCore.Signal(object)
    delete_filter_signal = QtCore.Signal(object)

    def __init__(self):
        super(filter_UI, self).__init__()

        self.setupUi()
        self.connect(self.save_b, QtCore.SIGNAL("clicked()"), self.update_filter)
        self.connect(self.hide_b, QtCore.SIGNAL("clicked()"), self.delete_filter)
        self.connect(self.key_2, QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.update_filter)
        self.connect(self.variavle_3, QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.update_filter)
        self.save_b.setHidden(True)
        self.width_default = 400
        self.height_default = 120
        self.variable_count = 4


    def set_variables(self, filter_data):
        # filter data -- [index, name, activate, filter_variables, avaliable_variables]
        # self.set_variable("key_filter", "not_set")
        # self.set_variable("active_variable", "not_set")
        # self.set_variable("split_char", "_")

        self.key_2.blockSignals(True)
        self.variavle_3.blockSignals(True)
        self.filter_index = filter_data[0]
        self.filter_name = filter_data[1]
        self.filter_activate = filter_data[2]
        self.filter_variables = filter_data[3]
        self.avaliable_variables = filter_data[4]
        self.key_filter, found1 = self.get_variable("key_filter")
        self.active_variable, found2 = self.get_variable("active_variable")
        self.split_char, found3 = self.get_variable("split_char")


        keys = tree_functions.get_all_current_keys()
        self.key_2.addItem("not_set")
        self.key_2.addItems(keys)
        self.variavle_3.addItem("not_set")
        self.variavle_3.addItems(self.avaliable_variables)

        index = self.key_2.findText(str(self.key_filter), QtCore.Qt.MatchFixedString)
        if index >= 0:
            self.key_2.setCurrentIndex(index)

        index = self.variavle_3.findText(str(self.active_variable), QtCore.Qt.MatchFixedString)
        if index >= 0:
            self.variavle_3.setCurrentIndex(index)
        self.key_2.blockSignals(False)
        self.variavle_3.blockSignals(False)

    # def get_keys(self):
    #     keys = []
    #     keys.append("not set")
    #     for file in os.listdir(ROOT_DIR + '/keys/'):
    #         if file.endswith(".key"):
    #             fsplit = file.split(".")
    #             keys.append(fsplit[0])
    #     return keys

    def update_filter(self):
        update = [str(self.filter_index), self.filter_name, self.filter_activate ,[["key_filter",str(self.key_2.currentText())], ["active_variable",str(self.variavle_3.currentText())], ["split_char", "_"]],[]]
        self.update_filter_signal.emit(update)
        #self.emit(SIGNAL("didSomething"), "important", "information")

    def delete_filter(self):
        #print "in delete filter (in filter)"
        to_delete = self.filter_name
        self.delete_filter_signal.emit(str(to_delete))

    def get_variable(self, attribute):
        found = False
        result = ""
        for filter_variable_tupple in self.filter_variables:
            if filter_variable_tupple[0] == attribute:
                result = filter_variable_tupple[1]
                found = True
        return result, found




    def setupUi(self):
        self.setObjectName("Form")
        self.resize(498, 122)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtGui.QFrame()
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtGui.QFrame(self.frame_2)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.hide_b = QtGui.QPushButton(self.frame)
        self.hide_b.setMaximumSize(QtCore.QSize(30, 16777215))
        self.hide_b.setObjectName("hide_b")
        self.horizontalLayout.addWidget(self.hide_b)
        self.name_1 = QtGui.QLabel(self.frame)
        self.name_1.setObjectName("name_1")
        self.horizontalLayout.addWidget(self.name_1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.save_b = QtGui.QPushButton(self.frame)
        self.save_b.setObjectName("save_b")
        self.horizontalLayout.addWidget(self.save_b)
        self.verticalLayout.addWidget(self.frame)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtGui.QLabel(self.frame_2)
        self.label_2.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.key_2 = QtGui.QComboBox(self.frame_2)
        self.key_2.setObjectName("key_2")
        self.horizontalLayout_2.addWidget(self.key_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtGui.QLabel(self.frame_2)
        self.label_3.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.variavle_3 = QtGui.QComboBox(self.frame_2)
        self.variavle_3.setObjectName("variavle_3")
        self.horizontalLayout_4.addWidget(self.variavle_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addWidget(self.frame_2)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.setLayout(self.verticalLayout_3)
        self.show()

    def retranslateUi(self):
        self.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.hide_b.setText(QtGui.QApplication.translate("Form", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.name_1.setText(QtGui.QApplication.translate("Form", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Key Filter:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Variable:", None, QtGui.QApplication.UnicodeUTF8))
        self.save_b.setText(QtGui.QApplication.translate("Form", "save", None, QtGui.QApplication.UnicodeUTF8))


        #self.setLayout(self.verticalLayout_3)
#self.show()