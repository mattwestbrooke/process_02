# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'combine_filter_UI.ui'
#
# Created: Sun Dec 18 14:05:55 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
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
        self.connect(self.var1_cb_3, QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.update_filter)
        self.connect(self.var2_cb_5, QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.update_filter)
        self.connect(self.var3_cb_7, QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.update_filter)
        self.new_var_8.editingFinished.connect(self.handle_le_sig)
        self.var1_le_2.editingFinished.connect(self.handle_le_sig)
        self.var2_le_4.editingFinished.connect(self.handle_le_sig)
        self.var3_le_6.editingFinished.connect(self.handle_le_sig)
        self.save_b.setHidden(True)
        self.width_default = 400
        self.height_default = 185
        self.variable_count = 9

    def handle_le_sig(self):
        if self.new_var_8.isModified() or self.var1_le_2.isModified() or self.var2_le_4.isModified() or self.var3_le_6.isModified():
            self.update_filter()


    def set_variables(self, filter_data):

        self.var1_cb_3.blockSignals(True)
        self.var2_cb_5.blockSignals(True)
        self.var3_cb_7.blockSignals(True)
        self.filter_index = filter_data[0]
        self.filter_name = filter_data[1]
        self.filter_activate = filter_data[2]
        self.filter_variables = filter_data[3]
        self.avaliable_variables = filter_data[4]
        self.text_1, found1 = self.get_variable("text_1")
        self.variable_1, found2 = self.get_variable("variable_1")
        self.text_2, found3 = self.get_variable("text_2")
        self.variable_2, found4 = self.get_variable("variable_2")
        self.text_3, found5 = self.get_variable("text_3")
        self.variable_3, found6 = self.get_variable("variable_3")
        self.result_variable, found7 = self.get_variable("result_variable")

        # self.var1_cb_3.blockSignals(True)
        # self.var2_cb_5.blockSignals(True)
        # self.var3_cb_7.blockSignals(True)

        # print "setting variables - ", filt_vars
        # print "in use container variables - ", vars
        # self.gfilt_vars = filter_data[1]

        #print "############### - gfilt CF - ", self.gfilt_vars
        self.var1_cb_3.addItem('not_set')
        self.var1_cb_3.addItems(self.avaliable_variables)
        self.var2_cb_5.addItem('not_set')
        self.var2_cb_5.addItems(self.avaliable_variables)
        self.var3_cb_7.addItem('not_set')
        self.var3_cb_7.addItems(self.avaliable_variables)

        index = self.var1_cb_3.findText(str(self.variable_1), QtCore.Qt.MatchFixedString)
        if index >= 0:
            self.var1_cb_3.setCurrentIndex(index)
        index = self.var2_cb_5.findText(str(self.variable_2), QtCore.Qt.MatchFixedString)
        if index >= 0:
            self.var2_cb_5.setCurrentIndex(index)
        index = self.var3_cb_7.findText(str(self.variable_3), QtCore.Qt.MatchFixedString)
        if index >= 0:
            self.var3_cb_7.setCurrentIndex(index)

        self.var1_le_2.setText(str(self.text_1))
        self.var2_le_4.setText(str(self.text_2))
        self.var3_le_6.setText(str(self.text_3))

        self.var1_cb_3.blockSignals(False)
        self.var2_cb_5.blockSignals(False)
        self.var3_cb_7.blockSignals(False)

        self.new_var_8.setText(self.result_variable)


    def get_keys(self):
        keys = []
        keys.append("not set")
        for file in os.listdir(ROOT_DIR + '/keys/'):
            if file.endswith(".key"):
                fsplit = file.split(".")
                keys.append(fsplit[0])
        #print "keys found - ", keys
        return keys

    # def update_vars(self):
    #     update = [str(self.name_1.text()), self.gfilt_vars, str(self.var1_le_2.text()), str(self.var1_cb_3.currentText()), str(self.var2_le_4.text()), str(self.var2_cb_5.currentText()), str(self.var3_le_6.text()), str(self.var3_cb_7.currentText()), str(self.new_var_8.text())]
    #     self.update_filter_signal.emit(update)

    def update_filter(self):
        print self.var1_le_2.text()
        print self.var2_le_4.text()
        print self.var3_le_6.text()
        print self.var1_cb_3.currentText()
        print self.var2_cb_5.currentText()
        print self.var3_cb_7.currentText()
        print self.new_var_8.text()

        update = [str(self.filter_index), self.filter_name, self.filter_activate ,[["text_1",str(self.var1_le_2.text())], ["text_2",str(self.var2_le_4.text())], ["text_3",str(self.var3_le_6.text())], ["variable_1",str(self.var1_cb_3.currentText())], ["variable_2",str(self.var2_cb_5.currentText())], ["variable_3",str(self.var3_cb_7.currentText())], ["result_variable",str(self.new_var_8.text())]],[]]
        self.update_filter_signal.emit(update)

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
        self.resize(536, 241)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtGui.QFrame()
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
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
        self.var1_le_2 = QtGui.QLineEdit(self.frame_2)
        self.var1_le_2.setMaximumSize(QtCore.QSize(450, 16777215))
        self.var1_le_2.setObjectName("var1_le_2")
        self.horizontalLayout_2.addWidget(self.var1_le_2)
        self.var1_cb_3 = QtGui.QComboBox(self.frame_2)
        self.var1_cb_3.setMinimumSize(QtCore.QSize(150, 0))
        self.var1_cb_3.setMaximumSize(QtCore.QSize(150, 16777215))
        self.var1_cb_3.setObjectName("var1_cb_3")
        self.horizontalLayout_2.addWidget(self.var1_cb_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtGui.QLabel(self.frame_2)
        self.label_3.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.var2_le_4 = QtGui.QLineEdit(self.frame_2)
        self.var2_le_4.setMaximumSize(QtCore.QSize(450, 16777215))
        self.var2_le_4.setObjectName("var2_le_4")
        self.horizontalLayout_3.addWidget(self.var2_le_4)
        self.var2_cb_5 = QtGui.QComboBox(self.frame_2)
        self.var2_cb_5.setMinimumSize(QtCore.QSize(150, 0))
        self.var2_cb_5.setMaximumSize(QtCore.QSize(150, 16777215))
        self.var2_cb_5.setObjectName("var2_cb_5")
        self.horizontalLayout_3.addWidget(self.var2_cb_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtGui.QLabel(self.frame_2)
        self.label_4.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.var3_le_6 = QtGui.QLineEdit(self.frame_2)
        self.var3_le_6.setMaximumSize(QtCore.QSize(450, 16777215))
        self.var3_le_6.setObjectName("var3_le_6")
        self.horizontalLayout_4.addWidget(self.var3_le_6)
        self.var3_cb_7 = QtGui.QComboBox(self.frame_2)
        self.var3_cb_7.setMinimumSize(QtCore.QSize(150, 0))
        self.var3_cb_7.setMaximumSize(QtCore.QSize(150, 16777215))
        self.var3_cb_7.setObjectName("var3_cb_7")
        self.horizontalLayout_4.addWidget(self.var3_cb_7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtGui.QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.new_var_8 = QtGui.QLineEdit(self.frame_2)
        self.new_var_8.setObjectName("new_var_8")
        self.horizontalLayout_5.addWidget(self.new_var_8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout_3.addWidget(self.frame_2)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.setLayout(self.verticalLayout_3)
        self.show()

    def retranslateUi(self):
        self.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.hide_b.setText(QtGui.QApplication.translate("Form", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.name_1.setText(QtGui.QApplication.translate("Form", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.save_b.setText(QtGui.QApplication.translate("Form", "save", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Variable1:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Variable2:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Variable3:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "New Variable Name:", None, QtGui.QApplication.UnicodeUTF8))

