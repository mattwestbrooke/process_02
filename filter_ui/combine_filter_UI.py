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
        self.connect(self.save_b, QtCore.SIGNAL("clicked()"), self.update_vars)
        self.connect(self.hide_b, QtCore.SIGNAL("clicked()"), self.delete_filter)
        self.connect(self.var1_cb_3, QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.update_vars)
        self.connect(self.var2_cb_5, QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.update_vars)
        self.connect(self.var3_cb_7, QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.update_vars)
        self.new_var_8.editingFinished.connect(self.handle_le_sig)
        self.var1_le_2.editingFinished.connect(self.handle_le_sig)
        self.var2_le_4.editingFinished.connect(self.handle_le_sig)
        self.var3_le_6.editingFinished.connect(self.handle_le_sig)
        self.save_b.setHidden(True)

    def handle_le_sig(self):
        if self.new_var_8.isModified() or self.var1_le_2.isModified() or self.var2_le_4.isModified() or self.var3_le_6.isModified():
            self.update_vars()


    def set_variables(self, filt_vars):

        self.var1_cb_3.blockSignals(True)
        self.var2_cb_5.blockSignals(True)
        self.var3_cb_7.blockSignals(True)

        # print "setting variables - ", filt_vars
        # print "in use container variables - ", vars
        self.gfilt_vars = filt_vars[1]

        print "############### - gfilt CF - ", self.gfilt_vars
        self.var1_cb_3.addItem('not_set')
        self.var1_cb_3.addItems(filt_vars[1])
        self.var2_cb_5.addItem('not_set')
        self.var2_cb_5.addItems(filt_vars[1])
        self.var3_cb_7.addItem('not_set')
        self.var3_cb_7.addItems(filt_vars[1])

        index = self.var1_cb_3.findText(str(filt_vars[3]), QtCore.Qt.MatchFixedString)
        if index >= 0:
            self.var1_cb_3.setCurrentIndex(index)
        index = self.var2_cb_5.findText(str(filt_vars[5]), QtCore.Qt.MatchFixedString)
        if index >= 0:
            self.var2_cb_5.setCurrentIndex(index)
        index = self.var3_cb_7.findText(str(filt_vars[7]), QtCore.Qt.MatchFixedString)
        if index >= 0:
            self.var3_cb_7.setCurrentIndex(index)

        self.var1_le_2.setText(filt_vars[2])
        self.var2_le_4.setText(filt_vars[4])
        self.var3_le_6.setText(filt_vars[6])

        self.var1_cb_3.blockSignals(False)
        self.var2_cb_5.blockSignals(False)
        self.var3_cb_7.blockSignals(False)

        self.new_var_8.setText(filt_vars[8])


    def get_keys(self):
        keys = []
        keys.append("not set")
        for file in os.listdir(ROOT_DIR + '/keys/'):
            if file.endswith(".key"):
                fsplit = file.split(".")
                keys.append(fsplit[0])
        #print "keys found - ", keys
        return keys

    def update_vars(self):
        update = [str(self.name_1.text()), self.gfilt_vars, str(self.var1_le_2.text()), str(self.var1_cb_3.currentText()), str(self.var2_le_4.text()), str(self.var2_cb_5.currentText()), str(self.var3_le_6.text()), str(self.var3_cb_7.currentText()), str(self.new_var_8.text())]
        self.update_filter_signal.emit(update)

    def delete_filter(self):
        #print "in delete filter (in filter)"
        to_delete = self.name_1.text()
        self.delete_filter_signal.emit(str(to_delete))




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

