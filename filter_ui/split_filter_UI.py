# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'split_filter_UI.ui'
#
# Created: Fri Dec 23 15:05:51 2016
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
        self.connect(self.var_2, QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.update_vars)
        self.connect(self.type_cb_4, QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.update_vars)
        self.split_cahr_3.editingFinished.connect(self.handle_le_sig)
        self.new_var_8.editingFinished.connect(self.handle_le_sig)
        self.save_b.setHidden(True)


    def handle_le_sig(self):
        if self.new_var_8.isModified() or self.split_cahr_3.isModified():
            self.update_vars()


    def set_variables(self, filt_vars):

        self.var_2.blockSignals(True)
        self.type_cb_4.blockSignals(True)

        # print "setting variables - ", filt_vars
        # print "in use container variables - ", vars
        self.gfilt_vars = filt_vars[1]

        #print "############### - gfilt CF - ", self.gfilt_vars
        self.var_2.addItem('not_set')
        self.var_2.addItems(filt_vars[1])

        index = self.var_2.findText(str(filt_vars[2]), QtCore.Qt.MatchFixedString)
        if index >= 0:
            self.var_2.setCurrentIndex(index)
        index = self.type_cb_4.findText(str(filt_vars[4]), QtCore.Qt.MatchFixedString)
        if index >= 0:
            self.type_cb_4.setCurrentIndex(index)

        self.split_cahr_3.setText(filt_vars[3])
        self.new_var_8.setText(filt_vars[5])

        self.var_2.blockSignals(False)
        self.type_cb_4.blockSignals(False)

        self.new_var_8.setText(filt_vars[5])
        if self.split_cahr_3.text() == "not_set" or filt_vars[3] == "not_set":
            self.split_cahr_3.setText("_")
            self.update_vars()

    def update_vars(self):
        update = [str(self.name_1.text()), self.gfilt_vars, str(self.var_2.currentText()), str(self.split_cahr_3.text()), str(self.type_cb_4.currentText()), str(self.new_var_8.text())]
        self.update_filter_signal.emit(update)

    def delete_filter(self):
        #print "in delete filter (in filter)"
        to_delete = self.name_1.text()
        self.delete_filter_signal.emit(str(to_delete))




    def setupUi(self):
        self.setObjectName("Form")
        self.resize(535, 173)
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
        self.label_2.setMaximumSize(QtCore.QSize(90, 16777215))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.var_2 = QtGui.QComboBox(self.frame_2)
        self.var_2.setObjectName("var_2")
        self.horizontalLayout_2.addWidget(self.var_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtGui.QLabel(self.frame_2)
        self.label_3.setMaximumSize(QtCore.QSize(90, 16777215))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.split_cahr_3 = QtGui.QLineEdit(self.frame_2)
        self.split_cahr_3.setMaximumSize(QtCore.QSize(30, 16777215))
        self.split_cahr_3.setObjectName("split_cahr_3")
        self.horizontalLayout_4.addWidget(self.split_cahr_3)
        self.label_4 = QtGui.QLabel(self.frame_2)
        self.label_4.setMaximumSize(QtCore.QSize(376, 16777215))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.type_cb_4 = QtGui.QComboBox(self.frame_2)
        self.type_cb_4.setObjectName("type_cb_4")
        self.type_cb_4.addItem("")
        self.type_cb_4.addItem("")
        self.type_cb_4.addItem("")
        self.horizontalLayout_4.addWidget(self.type_cb_4)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
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
        self.save_b.setText(QtGui.QApplication.translate("Form", "save", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Variable:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Split character: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Split Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.type_cb_4.setItemText(0, QtGui.QApplication.translate("Form", "first", None, QtGui.QApplication.UnicodeUTF8))
        self.type_cb_4.setItemText(1, QtGui.QApplication.translate("Form", "last", None, QtGui.QApplication.UnicodeUTF8))
        self.type_cb_4.setItemText(2, QtGui.QApplication.translate("Form", "all", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "New Variable Name:", None, QtGui.QApplication.UnicodeUTF8))

