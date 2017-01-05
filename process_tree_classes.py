import sys, os
from PySide.QtCore import *
from PySide.QtGui import *


class TreeTest(QTreeWidget):
    def __init__(self, parent=None):
        super(TreeTest, self).__init__(parent)
        self.setColumnCount(1)
        self.setHeaderLabel("Folders")

        actionEdit = QAction("New Folder", self)
        actionEdit.triggered.connect(self.addItemAction)
        self.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.addAction(actionEdit)

        actionDelete = QAction("Delete", self)
        actionDelete.triggered.connect(self.deleteItem)
        self.addAction(actionDelete)

        self.style()

    def addItem(self, name, parent):
        self.expandItem(parent)
        item = QTreeWidgetItem(parent)
        item.setText(0, name)
        # It is important to set the Flag Qt.ItemIsEditable
        item.setFlags(
            Qt.ItemIsSelectable | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled | Qt.ItemIsDragEnabled | Qt.ItemIsEditable)

        item.setIcon(0, self.style().standardIcon(QStyle.SP_DirIcon))
        return item

    def addItemAction(self):
        parent = self.currentItem()
        if parent is None:
            parent = self.invisibleRootItem()
        new_item = self.addItem("New Folder", parent)
        self.editItem(new_item)

    def addItemActionRoot(self):
        parent = self.currentItem()
        if parent is None:
            parent = self.invisibleRootItem()
        new_item = self.addItem("[root]", parent)
        self.editItem(new_item)

    def deleteItem(self):
        root = self.invisibleRootItem()
        for item in self.selectedItems():
            (item.parent() or root).removeChild(item)

    def getChildren(self, cur_root):
        child_count = cur_root.childCount()
        print "child_count - ", child_count
        children = []
        for i in range(child_count):
            itema = cur_root.child(i)
            folder_name = itema.text(0)
            children.append(folder_name)
        return  children

    def addPath(self, cur_root, adding_path):
        adding_path_split =  adding_path.split('/')
        this_root = cur_root
        for pp in adding_path_split:
            child_count = this_root.childCount()
            found = False
            for i in range(child_count):
                itema = this_root.child(i)
                folder_name = itema.text(0)
                if folder_name == pp:
                    found = True
                    new_level = itema
            if found == False:
                new_level = self.addItem(pp, this_root)
            this_root = new_level

    def addPathList(self, cur_root, adding_path_list):
        for jj in adding_path_list:
            self.addPath(cur_root, jj)

    def getParents(self, item):
        """
        Return a list containing all parent items of this item.
        The list is empty, if the item is a root item.
        """
        parents = []
        current_item = item
        current_parent = current_item.parent()

        # Walk up the tree and collect all parent items of this item
        while not current_parent is None:
            parents.append(current_parent)
            current_item = current_parent
            current_parent = current_item.parent()
        return parents

    def getParentsList(self, root):
        iterator = QTreeWidgetItemIterator(self)

        whole_tree = []

        while iterator.value():
            item = iterator.value()
            parents_names = []
            #print item.text(0)
            parents_names.append(str(item.text(0)))
            parents = self.getParents(item)
            for kk in parents:
                parents_names.append(str(kk.text(0)))
            parents_names.reverse()
            #print parents_names
            parents_names_string = ""
            for ll in parents_names[:-1]:
                parents_names_string = parents_names_string + ll
                parents_names_string = parents_names_string + '/'
            parents_names_string = parents_names_string + (parents_names[-1])
            #print parents_names_string
            whole_tree.append(parents_names_string)



            iterator += 1

        return whole_tree

