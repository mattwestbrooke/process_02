# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'make_folders_output_UI.ui'
#
# Created: Wed Feb 15 12:41:14 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!



from PySide import QtCore, QtGui
import sys
import os
import tree_functions

ROOT_DIR = os.path.dirname(sys.modules['__main__'].__file__)

class filter_UI(QtGui.QWidget):
    update_output_signal = QtCore.Signal(object)
    delete_output_signal = QtCore.Signal(object)

    def __init__(self):
        super(filter_UI, self).__init__()

        self.setupUi()
        self.connect(self.save_b, QtCore.SIGNAL("clicked()"), self.update_output)
        self.connect(self.hide_b, QtCore.SIGNAL("clicked()"), self.delete_output)
        self.connect(self.tree_cb, QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.update_output)
        self.save_b.setHidden(True)
        self.width_default = 700
        self.height_default = 100
        self.variable_count = 1

    def set_variables(self, filter_data):
        # filter data -- [index, name, activate, filter_variables, avaliable_variables]
        # self.set_variable("key_filter", "not_set")
        # self.set_variable("active_variable", "not_set")
        # self.set_variable("split_char", "_")

        self.tree_cb.blockSignals(True)
        self.output_index = filter_data[0]
        self.output_name = filter_data[1]
        self.output_variables = filter_data[2]
        #self.avaliable_variables = filter_data[3]

        self.current_tree, found1 = self.get_variable("tree")
        trees = tree_functions.get_all_current_trees()
        self.tree_cb.addItem("not_set")
        self.tree_cb.addItems(trees)

        index = self.tree_cb.findText(str(self.current_tree), QtCore.Qt.MatchFixedString)
        if index >= 0:
            self.tree_cb.setCurrentIndex(index)
        self.tree_cb.blockSignals(False)

    def update_output(self):
        update = [str(self.output_index), self.output_name, [["tree",str(self.tree_cb.currentText())]]]
        self.update_output_signal.emit(update)
        #self.emit(SIGNAL("didSomething"), "important", "information")

    def delete_output(self):
        #print "in delete filter (in filter)"
        to_delete = self.output_name
        self.delete_output_signal.emit(str(to_delete))

    def get_variable(self, attribute):
        found = False
        result = ""
        for output_variable_tupple in self.output_variables:
            if output_variable_tupple[0] == attribute:
                result = output_variable_tupple[1]
                found = True
        return result, found


    def setupUi(self):
        self.setObjectName("Form")
        self.resize(632, 108)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtGui.QFrame()
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame_2)
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
        self.tree_cb = QtGui.QComboBox(self.frame_2)
        self.tree_cb.setMinimumSize(QtCore.QSize(350, 0))
        self.tree_cb.setMaximumSize(QtCore.QSize(150, 16777215))
        self.tree_cb.setObjectName("tree_cb")
        self.horizontalLayout_2.addWidget(self.tree_cb)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
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
        self.label_2.setText(QtGui.QApplication.translate("Form", "Tree:", None, QtGui.QApplication.UnicodeUTF8))

