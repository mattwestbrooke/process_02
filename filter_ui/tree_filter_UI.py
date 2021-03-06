# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tree_filter_UI.ui'
#
# Created: Tue Dec 20 14:51:57 2016
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
        self.connect(self.tree_2, QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.update_vars)
        self.connect(self.tree_2, QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.update_paths)
        self.connect(self.path_3, QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.update_vars)
        self.new_var_8.editingFinished.connect(self.handle_le_sig)
        self.save_b.setHidden(True)

    def handle_le_sig(self):
        if self.new_var_8.isModified():
        #if self.new_var_8.isModified() or self.tree_2.isModified() or self.path_3.isModified():
            self.update_vars()


    def set_variables(self, filt_vars):

        self.tree_2.blockSignals(True)
        self.path_3.blockSignals(True)

        self.gfilt_vars = filt_vars[1]

        print "############### - gfilt CF - ", self.gfilt_vars
        trees, trees_paths = self.get_trees()

        self.tree_2.addItem('not_set')
        self.tree_2.addItems(trees)




        index = self.tree_2.findText(str(filt_vars[2]), QtCore.Qt.MatchFixedString)
        if index >= 0:
            self.tree_2.setCurrentIndex(index)
        if filt_vars[2] != "not set":
            paths = self.get_paths_from_tree(filt_vars[2])
            self.path_3.addItems(paths)

        index = self.path_3.findText(str(filt_vars[3]), QtCore.Qt.MatchFixedString)
        if index >= 0:
            self.path_3.setCurrentIndex(index)


        self.new_var_8.setText(filt_vars[4])

        self.tree_2.blockSignals(False)
        self.path_3.blockSignals(False)

        self.new_var_8.setText(filt_vars[4])


    def get_trees(self):
        trees = []
        trees_paths =[]
        #trees.append("not set")
        for file in os.listdir(ROOT_DIR + '/trees/'):
            file_path_a = ROOT_DIR + '/trees/'+file
            if file.endswith(".tree"):
                fsplit = file.split(".")
                trees.append(fsplit[0])
                our_path_list = []
                with open(file_path_a, 'r') as f:
                    for line in f:
                        our_path_list.append(str(line.rstrip()))
                trees_paths.append(our_path_list)
        print "TREES - ", trees
        print "TREES PATH - ", trees_paths
        return trees, trees_paths

    def get_paths_from_tree(self, tree):
        paths = []
        print "$$$$$$ tree - ", tree
        trees, trees_paths = self.get_trees()
        for i, j in enumerate(trees):
            if j == tree:
                paths = trees_paths[i]
        return paths

    def update_paths(self):
        self.path_3.clear()
        print "@#@#@ updating paths!!!"
        tree = self.tree_2.currentText()
        print "@#@#@ tree is - ", tree
        if tree != "" and tree != "not_set":
            paths = self.get_paths_from_tree(tree)
            print "paths -- ", paths
            self.path_3.addItems(paths)
        self.update_vars()


    def update_vars(self):
        update = [str(self.name_1.text()), self.gfilt_vars, str(self.tree_2.currentText()), str(self.path_3.currentText()), str(self.new_var_8.text())]
        self.update_filter_signal.emit(update)

    def delete_filter(self):
        to_delete = self.name_1.text()
        self.delete_filter_signal.emit(str(to_delete))




    def setupUi(self):
        self.setObjectName("Form")
        self.resize(537, 165)
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
        self.tree_2 = QtGui.QComboBox(self.frame_2)
        self.tree_2.setObjectName("tree_2")
        self.horizontalLayout_2.addWidget(self.tree_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtGui.QLabel(self.frame_2)
        self.label_3.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.path_3 = QtGui.QComboBox(self.frame_2)
        self.path_3.setObjectName("path_3")
        self.horizontalLayout_4.addWidget(self.path_3)
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
        self.label_2.setText(QtGui.QApplication.translate("Form", "tree filter:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "tree path:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "New Variable Name:", None, QtGui.QApplication.UnicodeUTF8))

