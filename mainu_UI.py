__appname__ = "PROCESS"



import atexit
import os
import shelve
import sys
import datetime

import tree_functions
import process_functions
import setups_functions
import data_input_functions
import defaults
import setup_object_classes

from PySide import QtCore, QtGui

import generic_ui.data_viewer_005_UI
import generic_ui.load_setup_UI
import generic_ui.process_mainUI_004 as main_dialog
from filter_ui import date_filter_UI, add_filter_UI, combine_filter_UI, key_filter_UI, split_filter_UI, tree_filter_UI
from outputs_ui import make_folders_output_UI, copy_folder_output_UI



ROOT_DIR = defaults.get_root_path()
UI_STATUS = defaults.get_ui_status()

class MainDialog(QtGui.QMainWindow, main_dialog.Ui_MainWindow ):
    """Main Dialog for the application
    """

    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)
        self.process_setup = setup_object_classes.Setup_Object("untitled")
        self.enable_ui_for_setup_loaded()
        self.set_type_buttons_from_input_type()
        self.filter_ui_dictionary = {'Key_Filter': key_filter_UI, 'Combine_Filter': combine_filter_UI}
        self.output_ui_dictionary = {'Make_Folders': make_folders_output_UI, 'Copy_Folder': copy_folder_output_UI}
        self.resize(890,950)


        ## GENERIC UI INIT

        atexit.register(self.save_process)
        self.current_setup_le.setEnabled(False)

        ## TREES UI INIT

        self.tree_tv.setDisabled(True)
        self.root_path_le.setDisabled(True)
        self.tree_name_label_2.setText("")
        self.connect(self.change_root_path_b, QtCore.SIGNAL("clicked()"), self.change_tree_root_path)
        self.connect(self.new_tree_b, QtCore.SIGNAL("clicked()"), self.new_tree)
        self.connect(self.remove_tree_b, QtCore.SIGNAL("clicked()"), self.delete_tree)
        self.connect(self.save_tree_b, QtCore.SIGNAL("clicked()"), self.save_tree)
        self.connect(self.new_variable_b, QtCore.SIGNAL("clicked()"), self.new_variable)
        self.connect(self.remove_variable_b, QtCore.SIGNAL("clicked()"), self.delete_variable)
        QtCore.QObject.connect(self.new_tree_lw, QtCore.SIGNAL("itemClicked(QListWidgetItem *)"), self.change_tree)
        self.populate_tree_list()

        ## KEYS UI INIT

        self.connect(self.new_key_b, QtCore.SIGNAL("clicked()"), self.new_key)
        self.connect(self.delete_key_b, QtCore.SIGNAL("clicked()"), self.delete_key)
        self.connect(self.new_constant_b, QtCore.SIGNAL("clicked()"), self.new_constant)
        self.connect(self.delete_constant_b, QtCore.SIGNAL("clicked()"), self.delete_constant)
        self.connect(self.constant_fiepath_te, QtCore.SIGNAL("clicked()"), self.set_constant_from_path)
        self.populate_keys()
        self.populate_constants()

        ## SETUPS AND OUTPUTS UI INIT

        self.set_file_input_le.setDisabled(True)
        self.current_setup_le.setText(self.process_setup.setup_name)
        self.connect(self.new_setup_b, QtCore.SIGNAL("clicked()"), self.new_setup)
        self.connect(self.save_setup_b, QtCore.SIGNAL("clicked()"), self.save_setup)
        self.connect(self.saveas_setup_b, QtCore.SIGNAL("clicked()"), self.save_setup_as)
        self.connect(self.load_setup_b, QtCore.SIGNAL("clicked()"), self.load_setup_by_ui)

        self.connect(self.set_file_input_b, QtCore.SIGNAL("clicked()"), self.set_file_input_path)
        self.connect(self.text_file_type_b, QtCore.SIGNAL("clicked()"), self.text_file_type_press)
        self.connect(self.folder_type_b, QtCore.SIGNAL("clicked()"), self.folder_type_press)
        self.connect(self.enter_text_type_b, QtCore.SIGNAL("clicked()"), self.enter_text_type_press)
        self.connect(self.xl_file_type_b, QtCore.SIGNAL("clicked()"), self.xl_file_type_press)

        self.set_file_input_le.editingFinished.connect(self.handle_file_input_sig)

        ## OUTPUTS UI

        self.connect(self.new_output_b_2, QtCore.SIGNAL("clicked()"), self.new_output)
        self.connect(self.refresh_outputs_b, QtCore.SIGNAL("clicked()"), self.refresh_outputs)
        self.connect(self.test_process_b, QtCore.SIGNAL("clicked()"), self.test_outputs)
        self.connect(self.submit_process_b, QtCore.SIGNAL("clicked()"), self.submit_outputs)
        self.populate_outputs_box()

        ## FILTERS UI

        self.connect(self.refresh_filters_b, QtCore.SIGNAL("clicked()"), self.refresh_filters)
        self.connect(self.new_filter_b, QtCore.SIGNAL("clicked()"), self.new_filter)
        self.populate_filters_box()
        self.refresh_outputs()

    ############ SIGNALS ########################

    def handle_file_input_sig(self):
        if self.set_file_input_le.isModified():
            self.update_type_data()

    ############ GENERIC ########################

    def save_process(self):
        self.save_setup()

    ############ SETUP UI FUNCTIONS #############

    def new_setup(self):
        new_setup_name = self.new_setup_le.text()
        if new_setup_name != "":
            if setups_functions.setup_exists(new_setup_name) == False:
                setups_functions.new_setup(new_setup_name)
            self.load_setup(new_setup_name)

    def load_setup(self, new_setup_name):
        print "-------------x in load setup"
        self.TESTPRINT()
        self.clear_all_setup_iu()
        self.current_setup_le.setText(new_setup_name)
        self.process_setup.load_setup(new_setup_name)
        self.enable_ui_for_setup_loaded()

    def enable_ui_for_setup_loaded(self):
        self.file_input_frame.setEnabled(True)
        self.tab_4.setEnabled(True)
        #self.tab_5.setEnabled(True)

    def disable_ui_for_setup_loaded(self):
        self.file_input_frame.setEnabled(False)
        self.tab_4.setEnabled(False)
        #self.tab_5.setEnabled(False)

    def load_setup_by_ui(self):
        print "-------------x in load setup by ui"
        self.TESTPRINT()
        dialog = New_Setup_Dialog()
        if dialog.exec_():
            our_procs = []
            for file in os.listdir(ROOT_DIR + '/setups/'):
                our_procs.append(file)
                #print file
            for proc_a in our_procs:
                dialog.load_process_lw.addItem(proc_a)
            selected = dialog.load_process_lw.currentItem().text()
            #print "we got as selected - ", selected
            selected_split = selected.split('.')
            self.load_setup(selected_split[0])

    def save_setup(self):
        print "-------------x in save setup"
        self.TESTPRINT()
        self.process_setup.save_setup()

    def save_setup_as(self):
        save_as_name = self.new_setup_le.text()
        if save_as_name != "":
            self.process_setup.save_setup_as(save_as_name)
            self.load_setup(save_as_name)

    def clear_all_setup_iu(self):
        self.current_setup_le.clear()
        self.set_file_input_le.clear()
        self.filters_le.clear()
        self.filters_lw.clear()
        self.data_object_lw.clear()
        self.outputs_lw.clear()
        self.new_setup_le.clear()


    ########### PROCESS TYPE UI FUNCTIONS #######


    def set_file_input_path(self):
        if self.process_setup.setup_input_type == "text_file":
            self.change_text_file_path()
            #print "setting - 0"
        elif self.process_setup.setup_input_type == "folder":
            self.change_folder_path()
            #print "setting - 1"
        elif self.process_setup.setup_input_type == "xl_file":
            self.change_xl_file_path()
            #print "setting - 3"
        self.refresh_filters()

    def text_file_type_press(self):
        self.process_setup.setup_input_type = "text_file"
        self.set_type_buttons_from_input_type()
        pass

    def folder_type_press(self):
        self.process_setup.setup_input_type = "folder"
        self.set_type_buttons_from_input_type()
        pass

    def enter_text_type_press(self):
        self.process_setup.setup_input_type = "enter_text"
        self.set_type_buttons_from_input_type()
        pass

    def xl_file_type_press(self):
        self.process_setup.setup_input_type = "xl_file"
        self.set_type_buttons_from_input_type()
        pass

    def set_type_buttons_from_input_type(self):
        if self.process_setup.setup_input_type == "text_file":
            self.text_file_f.setStyleSheet("background-color: green")
            self.folder_f.setStyleSheet("background-color: grey")
            self.enter_text_f.setStyleSheet("background-color: grey")
            self.xl_f.setStyleSheet("background-color: grey")

            # self.text_file_f.setVisible(True)
            # self.folder_f.setVisible(False)
            # self.enter_text_f.setVisible(False)
            # self.xl_f.setVisible(False)


            self.set_file_input_le.setText(self.process_setup.get_setup_input_data(0))
            self.set_file_input_b.setHidden(False)
            self.set_file_input_le.setDisabled(True)

        elif self.process_setup.setup_input_type == "folder":
            self.text_file_f.setStyleSheet("background-color: grey")
            self.folder_f.setStyleSheet("background-color: green")
            self.enter_text_f.setStyleSheet("background-color: grey")
            self.xl_f.setStyleSheet("background-color: grey")

            # self.text_file_f.setVisible(False)
            # self.folder_f.setVisible(True)
            # self.enter_text_f.setVisible(False)
            # self.xl_f.setVisible(False)


            self.set_file_input_le.setText(self.process_setup.get_setup_input_data(1))
            self.set_file_input_b.setHidden(False)
            self.set_file_input_le.setDisabled(True)

        elif self.process_setup.setup_input_type == "enter_text":
            self.text_file_f.setStyleSheet("background-color: grey")
            self.folder_f.setStyleSheet("background-color: grey")
            self.enter_text_f.setStyleSheet("background-color: green")
            self.xl_f.setStyleSheet("background-color: grey")

            # self.text_file_f.setVisible(False)
            # self.folder_f.setVisible(False)
            # self.enter_text_f.setVisible(True)
            # self.xl_f.setVisible(False)


            self.set_file_input_le.setText(self.process_setup.get_setup_input_data(2))
            self.set_file_input_b.setHidden(True)
            self.set_file_input_le.setDisabled(False)

        elif self.process_setup.setup_input_type == "xl_file":
            self.text_file_f.setStyleSheet("background-color: grey")
            self.folder_f.setStyleSheet("background-color: grey")
            self.enter_text_f.setStyleSheet("background-color: grey")
            self.xl_f.setStyleSheet("background-color: green")

            # self.text_file_f.setVisible(False)
            # self.folder_f.setVisible(False)
            # self.enter_text_f.setVisible(False)
            # self.xl_f.setVisible(True)


            self.set_file_input_le.setText(self.process_setup.get_setup_input_data(3))
            self.set_file_input_b.setHidden(False)
            self.set_file_input_le.setDisabled(True)

        self.update_type_data()

        self.save_setup()
        # self.refresh_filters()

    def update_type_data(self):
        if self.process_setup.setup_input_type == "text_file":
            self.process_setup.set_setup_input_data(self.set_file_input_le.text(), 0)
            #print "update - 0"
        elif self.process_setup.setup_input_type == "folder":
            self.process_setup.set_setup_input_data(self.set_file_input_le.text(), 1)
            #print "update - 1"
        elif self.process_setup.setup_input_type == "enter_text":
            self.process_setup.set_setup_input_data(self.set_file_input_le.text(), 2)
            #print "update - 2"
        elif self.process_setup.setup_input_type == "xl_file":
            self.process_setup.set_setup_input_data(self.set_file_input_le.text(), 3)
            #print "update - 3"

    def change_text_file_path(self):
        """ Change text file path for input type """

        if self.set_file_input_le.text() == "" or os.path.isdir(self.set_file_input_le.text()) == False:
            current_dir = os.getcwd()
        else:
            current_dir = self.root_path_le.text()
        fileObj = QtGui.QFileDialog.getOpenFileName(self, __appname__ + " Open File Dialog", dir=current_dir,
                                              filter="Input Text File (*.txt)")
        new_text_file = fileObj[0]
        if str(new_text_file) != "":
            self.set_file_input_le.setText(new_text_file)
            self.process_setup.set_setup_input_data(new_text_file, 0)
            self.save_setup()
        elif str(new_text_file) == "":
            return

    def change_folder_path(self):
        """ Change folderpath for input type """

        if self.set_file_input_le.text() == "" or os.path.isdir(self.set_file_input_le.text()) == False:
            current_dir = os.getcwd()
        else:
            current_dir = self.root_path_le.text()
        new_folder_path = str(QtGui.QFileDialog.getExistingDirectory(self, "Select Directory", current_dir))
        if str(new_folder_path) != "" and str(new_folder_path)[:13] != "/Applications" and str(new_folder_path)[
                                                                                       :10] != "/Developer" and str(
            new_folder_path)[:7] != "/System" and str(new_folder_path)[:8] != "/Library" and str(
            new_folder_path) != "/":
            self.set_file_input_le.setText(new_folder_path)
            self.process_setup.set_setup_input_data(new_folder_path, 1)
            self.save_setup()
        elif str(new_folder_path) == "":
            return

    def change_xl_file_path(self):
        """ Change xl file path for input type """

        if self.set_file_input_le.text() == "" or os.path.isdir(self.set_file_input_le.text()) == False:
            current_dir = os.getcwd()
        else:
            current_dir = self.root_path_le.text()
        fileObj = QtGui.QFileDialog.getOpenFileName(self, __appname__ + " Open File Dialog", dir=current_dir,
                                                    filter="Input Text File (*.xls)")
        new_text_file = fileObj[0]
        if str(new_text_file) != "":
            self.set_file_input_le.setText(new_text_file)
            self.process_setup.set_setup_input_data(new_text_file, 3)
            self.save_setup()
        elif str(new_text_file) == "":
            return


    ############ OUTPUT UI FUNCTIONS ############

    def new_output(self):
        print "-------------x in new output"
        self.TESTPRINT()
        new_output_type = str(self.new_output_cb_2.currentText())
        self.process_setup.output_object_list.create_new_output(new_output_type)
        self.process_setup.save_setup()
        self.refresh_outputs()

    def refresh_outputs(self):
        print "-------------x in refresh outputs"
        self.TESTPRINT()
        self.process_setup.load_setup(self.current_setup_le.text())

        input_list = self.get_input_list()
        if input_list != []:
            self.filters_lw.clear()
            self.outputs_lw.clear()
            self.refresh_data_objects(input_list)
            self.process_setup.data_object_list.filter_object_list.apply_filters(
                self.process_setup.data_object_list.data_object_list)
            avaliable_variables = self.process_setup.data_object_list.filter_object_list.get_variables_from_current_data_object_list(self.process_setup.data_object_list.data_object_list)
            self.process_setup.output_object_list.apply_outputs(avaliable_variables)
            if UI_STATUS == "yes":
                print "-------------x in ui setup --passed"
                self.TESTPRINT()
                self.refresh_data_UI()
                self.build_output_objects_UI()

    def test_outputs(self):
        pass

    def submit_outputs(self):
        pass

    def populate_outputs_box(self):
        outputs_dictionary = self.process_setup.output_object_list.output_types_dictionary
        filters = []
        for output_type in outputs_dictionary:
            filters.append(output_type)
        self.new_output_cb_2.addItems(filters)

    def build_output_objects_UI(self):
        print "-------------x in build filter objects UI"
        self.TESTPRINT()
        self.outputs_lw.clear()
        output_object_list = self.process_setup.output_object_list.output_object_list
        output_ui_dictionary = self.output_ui_dictionary
        #  [index, name, activate, filter_variables, avaliable_variables]
        #  new_output_object = self.output_types_dictionary[output_type](new_index, new_name)
        # print "--x our filters"
        # self.process_setup.data_object_list.filter_object_list.temp_print_filter_data()
        # print "--x all printed"
        for output in output_object_list:
            output_data = output.get_full_data()
            output_name = output_data[1]
            output_type = ((output_name).split('-'))[0]
            new_output_UI_object = output_ui_dictionary[output_type].filter_UI()

            new_output_UI_object.update_output_signal.connect(self.update_output)
            new_output_UI_object.delete_output_signal.connect(self.delete_output)

            new_output_UI_object.name_1.setText(output_name)
            new_output_UI_object.set_variables(output_data)

            new_filter_UI_widget = QtGui.QListWidgetItem()
            new_filter_UI_widget.setSizeHint(QtCore.QSize(new_output_UI_object.width_default, new_output_UI_object.height_default))
            self.outputs_lw.addItem(new_filter_UI_widget)
            self.outputs_lw.setItemWidget(new_filter_UI_widget, new_output_UI_object)

    def update_output(self, output_data):
        # print "in update filter"
        #  [index, name, activate, filter_variables, avaliable_variables]
        # self.process_setup.data_object_list.filter_object_list.temp_print_filter_data()
        output = self.process_setup.output_object_list.find_output_from_name(output_data[1])
        for tupple in output_data[2]:
            output.set_variable(tupple[0], tupple[1])
        self.process_setup.save_setup()

    def delete_output(self, output_to_delete):
        # print "in delete filter"
        # print "filter to delete = ", filter_to_delete
        outputs_list = self.process_setup.output_object_list.get_full_output_list()
        length = len(outputs_list)
        # print "length - ", length
        index = "none"
        for kk in range(0, length):
            # print "---X ", filters_list[kk][1]
            if outputs_list[kk][1] == output_to_delete:
                index = kk
        if index != "none":
            # print "found our filter --"
            del outputs_list[index]
            # print "new_filters list = ", filters_list
            full_filename, can_create = setups_functions.get_setup_path(self.process_setup.setup_name)
            if os.path.exists(full_filename):
                self.process_setup.output_object_list.shelve_output_list_from_list(outputs_list, full_filename)
                self.process_setup.output_object_list.load_output_list_from_file(full_filename)
                self.build_output_objects_UI()



    ############ FILTER UI FUNCTIONS ############

    def TESTPRINT(self):
        self.process_setup.print_TEST_current_data_filter_outputs()

    def populate_filters_box(self):
        filters_dictionary = self.process_setup.data_object_list.filter_object_list.filter_types_dictionary
        filters = []
        for filter_type in filters_dictionary:
            filters.append(filter_type)
        self.new_filter_cb.addItems(filters)

        self.refresh_filters()

    def new_filter(self):
        print "-------------x in new filter"
        self.TESTPRINT()
        new_filter_type = str(self.new_filter_cb.currentText())
        self.process_setup.data_object_list.filter_object_list.create_new_filter(new_filter_type)
        self.process_setup.save_setup()
        self.refresh_filters()

    def refresh_filters(self):
        print "-------------x in refresh filters"
        self.TESTPRINT()
        self.process_setup.load_setup(self.current_setup_le.text())

        input_list = self.get_input_list()
        if input_list != []:
            self.filters_lw.clear()
            self.refresh_data_objects(input_list)
            self.process_setup.data_object_list.filter_object_list.apply_filters(self.process_setup.data_object_list.data_object_list)
            if UI_STATUS == "yes":
                print "-------------x in ui setup --passed"
                self.TESTPRINT()
                self.refresh_data_UI()

    def refresh_data_objects(self, input_list):
        print "-------------x in refresh data_objects"
        self.TESTPRINT()
        self.process_setup.data_object_list.setup_data_objects_from_input_list(input_list)

    def get_input_list(self):
        input_type = self.process_setup.get_setup_input_type()
        input_list = []
        if input_type == "text_file":
            if os.path.exists(self.set_file_input_le.text()):
                input_list = data_input_functions.get_input_list_from_text_file(self.set_file_input_le.text())
        elif self.process_setup.setup_input_type == "folder":
            print "not coded yet"
            input_list = []
        elif self.process_setup.setup_input_type == "enter_text":
            print "not coded yet"
            input_list = []
        elif self.process_setup.setup_input_type == "xl_file":
            print "not coded yet"
        #print "input_list --- ", input_list
        return input_list

    def refresh_data_UI(self):
        print "-------------x refresh data UI"
        self.TESTPRINT()
        self.build_data_objects_UI()
        self.build_filter_objects_UI()

    def build_data_objects_UI(self):
        print "-------------x populate data widgets UI"
        self.TESTPRINT()
        self.data_object_lw.clear()
        data_object_list = self.process_setup.data_object_list.data_object_list
        for data_object in data_object_list:
            data_object_UI = generic_ui.data_viewer_005_UI.Dv_005()
            data_object_UI.label.setText(str(data_object.get_index()))
            vars = data_object.get_variable_tupples()
            for var in range(0, len(vars)):
                data_object_UI.set_variable(vars[var][0], vars[var][1])

            data_object_UI.populate_list()
            data_object_widget = QtGui.QListWidgetItem()
            data_object_widget.setSizeHint(QtCore.QSize(600, (32 + ((len(vars)) * 32))))
            self.data_object_lw.addItem(data_object_widget)
            self.data_object_lw.setItemWidget(data_object_widget, data_object_UI)

    def build_filter_objects_UI(self):
        print "-------------x in build filter objects UI"
        self.TESTPRINT()
        self.filters_lw.clear()
        filter_object_list = self.process_setup.data_object_list.filter_object_list.filter_object_list
        filter_ui_dictionary = self.filter_ui_dictionary
        #  [index, name, activate, filter_variables, avaliable_variables]
        #  new_output_object = self.output_types_dictionary[output_type](new_index, new_name)
        # print "--x our filters"
        # self.process_setup.data_object_list.filter_object_list.temp_print_filter_data()
        # print "--x all printed"
        for filter in filter_object_list:
            filter_data = filter.get_full_data()
            filter_name = filter_data[1]
            filter_type = ((filter_name).split('-'))[0]
            new_filter_UI_object = filter_ui_dictionary[filter_type].filter_UI()

            new_filter_UI_object.update_filter_signal.connect(self.update_filter)
            new_filter_UI_object.delete_filter_signal.connect(self.delete_filter)

            new_filter_UI_object.name_1.setText(filter_name)
            new_filter_UI_object.set_variables(filter_data)

            new_filter_UI_widget = QtGui.QListWidgetItem()
            new_filter_UI_widget.setSizeHint(QtCore.QSize(new_filter_UI_object.width_default, new_filter_UI_object.height_default))
            self.filters_lw.addItem(new_filter_UI_widget)
            self.filters_lw.setItemWidget(new_filter_UI_widget, new_filter_UI_object)

    def update_filter(self, filter_data):
        # print "in update filter"
        #  [index, name, activate, filter_variables, avaliable_variables]
        # self.process_setup.data_object_list.filter_object_list.temp_print_filter_data()
        filter = self.process_setup.data_object_list.filter_object_list.find_filter_from_name(filter_data[1])
        for tupple in filter_data[3]:
            filter.set_variable(tupple[0], tupple[1])
        self.process_setup.save_setup()

    def delete_filter(self, filter_to_delete):
        #print "in delete filter"
        #print "filter to delete = ", filter_to_delete
        filters_list = self.process_setup.data_object_list.filter_object_list.get_full_filter_list()
        length = len(filters_list)
        #print "length - ", length
        index = "none"
        for kk in range(0, length):
            #print "---X ", filters_list[kk][1]
            if filters_list[kk][1] == filter_to_delete:
                index = kk
        if index != "none":
            #print "found our filter --"
            del filters_list[index]
            #print "new_filters list = ", filters_list
            full_filename, can_create = setups_functions.get_setup_path(self.process_setup.setup_name)
            if os.path.exists(full_filename):
                self.process_setup.data_object_list.filter_object_list.shelve_filter_list_from_list(filters_list, full_filename)
                self.process_setup.data_object_list.filter_object_list.load_filter_list_from_file(full_filename)
                self.build_filter_objects_UI()












    ############ TREE UI FUNCTIONS ##############

    def change_tree(self):
        new_tree = self.new_tree_lw.currentItem().text()
        self.open_tree(new_tree)

    def enable_tree(self):
        self.tree_tv.setDisabled(False)
        self.root_path_le.setDisabled(False)

    def disable_tree(self):
        self.tree_tv.setDisabled(True)
        self.root_path_le.setDisabled(True)

    def change_tree_root_path(self):
        """ Change tree root path """

        if self.root_path_le.text() == "" or os.path.isdir(self.root_path_le.text()) == False:
            current_dir = os.getcwd()
        else:
            current_dir = self.root_path_le.text()
        new_root_path = str(QtGui.QFileDialog.getExistingDirectory(self, "Select Directory", current_dir))
        if str(new_root_path) != "" and str(new_root_path)[:13] != "/Applications" and str(new_root_path)[
                                                                                       :10] != "/Developer" and str(
                new_root_path)[:7] != "/System" and str(new_root_path)[:8] != "/Library" and str(
                new_root_path) != "/":
            self.root_path_le.setText(new_root_path)
        elif str(new_root_path) == "":
            return

    def populate_tree_list(self):
        our_trees = tree_functions.get_all_current_trees()
        self.new_tree_lw.clear()
        for ll in our_trees:
            self.new_tree_lw.addItem(ll)

    def new_tree(self):
        if self.new_tree_le.text() != "":
            self.populate_tree_list()
            self.enable_tree()
            if self.tree_name_label_2 != "":
                self.save_tree()
            #fname, fname_root, fname_varb, new_name_ext, new_name = tree_functions.get_new_tree_variables(self.new_tree_le.text())
            new_name = self.new_tree_le.text()
            if tree_functions.tree_exists(new_name) == False:
                tree_functions.make_new_tree(new_name)
                self.tree_tv.clear()
                self.tree_tv.addItemActionRoot()
                self.tree_name_label_2.setText((new_name + ".tree"))
                self.save_tree()
                self.populate_tree_list()
                self.populate_variable_list()
            else:
                self.open_tree(new_name)
                self.populate_variable_list()

    def open_tree(self, tree_name):
        if self.tree_name_label_2 != "":
            self.save_tree()
        self.enable_tree()
        #print "open - " + tree_name
        self.tree_name_label_2.setText((tree_name + ".tree"))
        our_tree_file = ROOT_DIR + '/trees/' + tree_name + ".tree"
        our_root_file = (os.path.splitext(our_tree_file)[0]) + '.root'
        with open(our_root_file, 'r') as ff:
            for liner in ff:
                self.root_path_le.setText(str(liner.rstrip()))

        if os.path.exists(our_tree_file) == True:
            our_tree_list = []
            with open(our_tree_file, 'r') as f:
                for line in f:
                    our_tree_list.append(str(line.rstrip()))
                    #print "line - ",line
                    if 'str' in line:
                        break
            root = self.tree_tv.invisibleRootItem()
            self.tree_tv.clear()
            self.tree_tv.addPathList(root, our_tree_list)
        else:
            print "path no exist"
        self.populate_variable_list()

    def open_tree2(self):

        if self.tree_name_label_2 != "":
            self.save_tree()
        self.enable_tree()
        treename  = self.new_tree_le.text()
        #print "open - " + treename
        self.tree_name_label_2.setText((treename + ".tree"))
        our_tree_file = ROOT_DIR + '/trees/' + treename + ".tree"
        our_root_file = (os.path.splitext(our_tree_file)[0]) + '.root'
        with open(our_root_file, 'r') as ff:
            for liner in ff:
                self.root_path_le.setText(str(liner.rstrip()))

        if os.path.exists(our_tree_file) == True:
            our_tree_list = []
            with open(our_tree_file, 'r') as f:
                for line in f:
                    our_tree_list.append(str(line.rstrip()))
                    # print "line - ",line
                    if 'str' in line:
                        break
            root = self.tree_tv.invisibleRootItem()
            self.tree_tv.clear()
            # print "tree list - ", our_tree_list
            self.tree_tv.addPathList(root, our_tree_list)
        else:
            print "path no exist"
        self.populate_variable_list()

    def save_tree(self):
        if self.tree_name_label_2.text() != "":
            save_tree_path = ROOT_DIR + '/trees/' + self.tree_name_label_2.text()
            save_root_path_path = (os.path.splitext(save_tree_path)[0]) + '.root'
            open(save_root_path_path, 'w')
            with open(save_root_path_path, "a") as save_root_file:
                save_root_file.write(self.root_path_le.text() + "\n")

            # print "base path - ", save_root_path_path
            open(save_tree_path, 'w')
            root = self.tree_tv.invisibleRootItem()
            save_trees_content = self.tree_tv.getParentsList(root)
            # print "saved_values - ", save_trees_content
            with open(save_tree_path, "a") as save_tree_file:
                for jj in save_trees_content:
                    save_tree_file.write(str(jj) + "\n")
            self.populate_variable_list()

    def delete_tree(self):
        remove_tree  = self.new_tree_lw.currentItem().text()
        if remove_tree != "":
            os.remove(ROOT_DIR + '/trees/' + remove_tree + ".tree")
            os.remove(ROOT_DIR + '/trees/' + remove_tree + ".root")
            os.remove(ROOT_DIR + '/trees/' + remove_tree + ".varb")
        self.populate_tree_list()
        self.tree_tv.clear()
        self.tree_name_label_2.setText("")
        self.root_path_le.setText("")
        self.disable_tree()
        self.populate_variable_list()

    def new_variable(self):
        if self.new_variabl_le.text() != "" and self.tree_name_label_2.text() != "":
            self.populate_variable_list()
            splt = self.tree_name_label_2.text()
            spl = splt.split('.')
            fname_varb = ROOT_DIR + '/trees/' + spl[0] + ".varb"

            make_new = True
            current_varbs = []
            with open(fname_varb, 'r') as ff:
                for linerr in ff:
                    if linerr.rstrip() == self.new_variabl_le.text():
                        make_new = False
                        # print "found previous!!"
            if make_new == True:

                with open(fname_varb, 'a') as fff:
                    fff.write(str(self.new_variabl_le.text()) + "\n")
                self.populate_variable_list()
            elif make_new == False:
                print "variable already exists"

    def delete_variable(self):
        remove_variable  = self.new_variable_lw.currentItem().text()
        if remove_variable != "" and self.tree_name_label_2.text() != "":
            splt = self.tree_name_label_2.text()
            spl = splt.split('.')
            fname_varb = ROOT_DIR + '/trees/' + spl[0] + ".varb"
            varbs_hold = []
            with open(fname_varb, 'r') as ff:
                for linerr in ff:
                    varbs_hold.append(linerr.rstrip())
            if remove_variable in varbs_hold:
                varbs_hold.remove(remove_variable)
            open(fname_varb, 'w')
            with open(fname_varb, "a") as save_varb_file:
                for gg in varbs_hold:
                    save_varb_file.write(gg + "\n")
            self.populate_variable_list()

    def populate_variable_list(self):
        if self.tree_name_label_2.text() != "":
            our_varbs = []
            splt = self.tree_name_label_2.text()
            spl = splt.split('.')
            fname_varb = ROOT_DIR + '/trees/' + spl[0] + ".varb"
            with open(fname_varb, 'r') as ff:
                for linerr in ff:
                    our_varbs.append(linerr)
            self.new_variable_lw.clear()
            for ll in our_varbs:
                self.new_variable_lw.addItem(ll.rstrip())
        else:
            self.new_variable_lw.clear()

    ############ KEYS AND CONSTANTS UI FUNCTIONS ##############

    def set_constant_from_path(self):
        # print "set constant from path"
        if self.new_constant_name_leconstant_te.text() == "" or os.path.isdir(self.constant_te.text()) == False:
            current_dir = os.getcwd()
        else:
            current_dir = self.root_path_le.text()
        new_root_path = str(QtGui.QFileDialog.getExistingDirectory(self, "Select Directory",current_dir))
        if str(new_root_path) != "" and str(new_root_path)[:13] != "/Applications" and str(new_root_path)[:10] != "/Developer" and str(new_root_path)[:7] != "/System" and str(new_root_path)[:8] != "/Library" and str(new_root_path) != "/":
            self.constant_te.setText(new_root_path)
        elif str(new_root_path) == "":
            return

    def new_key(self):
        if self.new_key_name_le.text() == "" or self.key_te.text() == "":
            print "cannot add key"
        else:
            fname_k = ROOT_DIR + '/keys/' + self.new_key_name_le.text() + ".key"
            open(fname_k, 'w')
            with open(fname_k, "a") as save_key_file:
                save_key_file.write(self.key_te.text())
        self.populate_keys()

    def populate_keys(self):
        #print "populating keys"
        self.keys_tw.setRowCount(0)
        #self.keys_tw.setColumnCount(0)
        our_keys = []
        for file in os.listdir(ROOT_DIR + '/keys/'):
            if file.endswith(".key"):
                fsplit = file.split(".")
                with open((ROOT_DIR + '/keys/'+file), 'r') as f:
                    for line in f:
                        key_tx = str(line.rstrip())
                our_keys.append([fsplit[0], key_tx])
                # print our_keys
        for ll in our_keys:
            rowPosition = self.keys_tw.rowCount()
            self.keys_tw.insertRow(rowPosition)
            self.keys_tw.setItem(rowPosition, 0, QtGui.QTableWidgetItem(ll[0]))
            self.keys_tw.setItem(rowPosition, 1, QtGui.QTableWidgetItem(ll[1]))
        self.keys_tw.resizeColumnsToContents()

    def delete_key(self):
        # print "delete key"
        remove_key = self.keys_tw.currentItem().text()
        # print "testing - ", remove_key
        del_fname = ROOT_DIR + '/keys/' + remove_key + '.key'
        if os.path.exists(del_fname) == True:
            os.remove(del_fname)
            self.populate_keys()

    def new_constant(self):
        if self.new_constant_name_le.text() == "" or self.constant_te.text() == "":
            print "cannot add constant"
        else:
            fname_c = ROOT_DIR + '/constants/' + self.new_constant_name_le.text() + ".const"
            open(fname_c, 'w')
            with open(fname_c, "a") as save_con_file:
                save_con_file.write(self.constant_te.text())
        self.populate_constants()

    def populate_constants(self):
        #print "populating keys"
        self.constants_tw.setRowCount(0)
        # self.keys_tw.setColumnCount(0)
        our_cons = []
        for file in os.listdir(ROOT_DIR + '/constants/'):
            if file.endswith(".const"):
                fsplit = file.split(".")
                with open((ROOT_DIR + '/constants/' + file), 'r') as f:
                    for line in f:
                        con_tx = str(line.rstrip())
                our_cons.append([fsplit[0], con_tx])
                # print our_cons
        for ll in our_cons:
            rowPosition = self.constants_tw.rowCount()
            self.constants_tw.insertRow(rowPosition)
            self.constants_tw.setItem(rowPosition, 0, QtGui.QTableWidgetItem(ll[0]))
            self.constants_tw.setItem(rowPosition, 1, QtGui.QTableWidgetItem(ll[1]))
        self.constants_tw.resizeColumnsToContents()

    def delete_constant(self):
        # print "delete key"
        remove_con = self.constants_tw.currentItem().text()
        # print "testing - ", remove_con
        del_fname = ROOT_DIR + '/constants/' + remove_con + '.const'
        if os.path.exists(del_fname) == True:
            os.remove(del_fname)
            self.populate_constants()



class New_Setup_Dialog(QtGui.QDialog, generic_ui.load_setup_UI.Ui_Dialog):

    def __init__(self, parent=None):
        super(New_Setup_Dialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Load Setup")

        our_procs = []
        for file in os.listdir(ROOT_DIR + '/setups/'):
            our_procs.append(file)
            #print file
        for proc_a in our_procs:
            self.load_process_lw.addItem(proc_a)







app = QtGui.QApplication(sys.argv)
form = MainDialog()
form.show()
app.exec_()