import defaults
import setups_functions
import data_object_classes
import output_object_classes
import shelve
import os

ROOT_DIR = defaults.get_root_path()
UI_STATUS = defaults.get_ui_status()

class Setup_Object(object):

    def __init__(self, setup):
        self.setup_name = setup
        self.setup_path_name, can_create = setups_functions.get_setup_path(setup)
        self.setup_input_type = "textfile"
        self.setup_input_data = ["", "", "", ""]
        self.data_object_list = data_object_classes.Data_Object_List()
        self.output_object_list = output_object_classes.Output_Object_List(self.data_object_list)
        if self.setup_exists(setup) == True:
            self.load_setup(setup)
        else:
            if self.setup_exists("untitled") == True:
                self.load_setup("untitled")
            else:
                setups_functions.new_setup("untitled")
                self.load_setup("untitled")

    def set_names(self, new_setup):
        self.setup_name = new_setup
        self.setup_path_name, can_create = setups_functions.get_setup_path(self.setup_name)

    def get_name(self):
        return self.setup_name

    def setup_exists(self, setup):
        path_name, can_create = setups_functions.get_setup_path(setup)
        if can_create == False:
            return True
        else:
            return False

    def set_setup_input_type(self, input_type):
        self.setup_input_type = input_type

    def get_setup_input_type(self):
        return self.setup_input_type

    def set_setup_input_data(self, data, index):
        self.setup_input_data[index] = data

    def get_setup_input_data(self, index):
        #print 'index - ', index
        return self.setup_input_data[index]

    def load_setup(self, setup):
        load_setup_path, create_new = setups_functions.get_setup_path(setup)
        #print "path -- ", load_setup_path
        setups_functions.load_file_to_setup(load_setup_path, self.data_object_list, self.output_object_list)
        self.set_names(setup)
        self.setup_input_type = setups_functions.load_input_type(load_setup_path)
        self.setup_input_data = setups_functions.load_input_data(load_setup_path)

    def save_setup(self):
        setups_functions.save_setup_to_file(self.setup_path_name, self.data_object_list, self.output_object_list)
        setups_functions.save_input_type(self.setup_path_name, self.setup_input_type)
        setups_functions.save_input_data(self.setup_path_name, self.setup_input_data)

    def save_setup_as(self, new_name):
        #print "setup -- name --- ", new_name
        setups_functions.new_setup(new_name)
        new_setup_path, creat_new =  setups_functions.get_setup_path(new_name)
        setups_functions.save_setup_to_file(new_setup_path, self.data_object_list, self.output_object_list)
        setups_functions.save_input_type(new_setup_path, self.setup_input_type)
        setups_functions.save_input_data(new_setup_path, self.setup_input_data)
        self.load_setup(new_name)

    def print_TEST_current_data_filter_outputs(self):
        print "####### CURRENT SETUP DATA #######"
        setups_functions.print_setup_contents(self.setup_name)
        print ""
        print "####### DATA OBJECTS #############"
        self.data_object_list.temp_print_data_objects()
        print ""
        print "####### FILTER OBJECTS ###########"
        self.data_object_list.filter_object_list.temp_print_filter_data()
        print ""
        print "####### OUTPUT OBJECTS ###########"
        self.output_object_list.temp_print_output_data()
        print ""



