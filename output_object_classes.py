import tree_functions
import process_functions
import shelve
import os
from time import gmtime, strftime


class Output_Object_List(object):

    def __init__(self, data_object_list):
        self.data_objects = data_object_list.get_data_objects()
        self.data_object_list = data_object_list
        self.output_object_list = []
        self.output_types_dictionary = {'Make_Folders': Output_Make_Folders, 'Copy_Folder': Output_Copy_Folder}

    def create_new_output(self, output_type):
        """makes new output no data just from type"""
        new_index = self.get_next_index()
        new_name = self.get_new_name(output_type)
        new_output_object = self.output_types_dictionary[output_type](new_index, new_name)
        self.add_new_object_to_object_list(new_output_object)

    def create_new_output_apply_data(self, output_type, data):
        """ makes a new output object from shelved data
        data example - [0, 'Make_Folders-1', [['tree', '']]] ... [index, name, [variables, ..]]
        """
        new_index = self.get_next_index()
        new_name = data[1]
        new_variables = data[2]
        new_output_object = self.output_types_dictionary[output_type](new_index, new_name)
        new_output_object.set_output_name(new_name)
        new_output_object.set_all_variables(new_variables)
        self.add_new_object_to_object_list(new_output_object)

    def temp_print_output_data(self):
        print "current object data -"
        for obj in self.output_object_list:
            print str(obj.get_full_data())

    def add_new_object_to_object_list(self, new_output_object):
        new_output_object.set_index(self.get_next_index())
        self.output_object_list.append(new_output_object)

    def get_next_index(self):
        length = len(self.output_object_list)
        return length

    def shelve_output_list_as_file(self, full_filename):
        #print "saving shelving output list - ", full_filename
        output_object_data_list = []
        for output_object in self.output_object_list:
            data = output_object.get_full_data()
            #print "shelving data - ", data
            output_object_data_list.append(data)
        shelve_file = shelve.open(full_filename)
        shelve_file['output_object_list'] = output_object_data_list
        shelve_file.close()

    def shelve_output_list_from_list(self, output_object_data_list, full_filename):
        shelve_file = shelve.open(full_filename)
        shelve_file['output_object_list'] = output_object_data_list
        shelve_file.close()

    def load_output_list_from_file(self, full_filename):
        print "loading shelved output list - ", full_filename
        self.output_object_list = []
        shelve_file = shelve.open(full_filename)
        output_object_data_list = shelve_file['output_object_list']
        shelve_file.close()
        for data in output_object_data_list:
            type = self.get_output_type_from_name(data[1])
            self.create_new_output_apply_data(type, data)

    def get_output_type_from_name(self, name):
        name_split = name.split('-')
        return name_split[0]

    def get_all_current_names(self):
        current_names = []
        for object in self.output_object_list:
            current_names.append(object.get_output_name())
        return current_names

    def get_new_name(self, output_type):
        current_names = self.get_all_current_names()
        counter = 1
        ok_new = False
        while ok_new != True:
            try_name = output_type + "-" + str(counter)
            if try_name not in current_names:
                new_name = try_name
                ok_new = True
            counter = counter + 1
        return new_name

    def get_full_output_list(self):
        full_output_list = []
        for obj in self.output_object_list:
            full_output_list.append(obj.get_full_data())
        return full_output_list

    def find_output_from_name(self, output_name):
        found_output = False
        for output in self.output_object_list:
            if output.get_output_name() == output_name:
                found_output = output
        return found_output

    def find_output_from_name(self, output_name):
        found_output = False
        for output in self.output_object_list:
            if output.get_output_name() == output_name:
                found_output = output
        return found_output

    def set_output_variable_from_output_name(self, variable, value, output_name):
        output = self.find_output_from_name(output_name)
        if output != False:
            output.set_variable(variable, value)

    def set_process_data_to_file(self, process_name):
        new_process_name = process_functions.get_new_process_name(process_name)
        new_process_file_path = process_functions.new_process_file(new_process_name)
        process = []
        for output in self.output_object_list:
            process_output = output.setup_process_output(self.data_object_list)
            process.append(process_output)
        process_functions.set_process_data_to_file(new_process_file_path, process)

    def apply_outputs(self, avaliable_variables):
        for output in self.output_object_list:
            output.apply_avaliable_variables(avaliable_variables)

class Output_Object(object):

    def __init__(self, index, name):
        self.index = index
        self.variables = []
        self.avaliable_variables = []
        self.name = name

    def set_index(self, index):
        self.index = index

    def get_index(self):
        return self.index

    def set_output_name(self, name):
        self.name = name

    def get_output_name(self):
        return self.name

    def set_all_variables(self, variables):
        self.variables = variables

    def get_all_variables(self):
        return self.variables

    def set_variable(self, attribute, value):
        found = False
        for variable in self.variables:
            if variable[0] == attribute:
                variable[1] = value
                found = True

        if found == False:
            self.variables.append([attribute, value])
        return found

    def get_variable(self, attribute):
        found = False
        result = ""
        for variable in self.variables:
            if variable[0] == attribute:
                result = variable[1]
                found = True
        return result, found

    def get_full_data(self):
        return [self.index, self.name, self.variables]

    def set_full_data(self, index, name, variables):
        self.index = index
        self.name = name,
        self.variables = variables

    def shelve_output_as_file(self, full_filename):
        """makes static data file from output object"""
        shelve_file = shelve.open(full_filename)
        shelve_file['index'] = self.index
        shelve_file['name'] = self.name
        shelve_file['variables'] = self.variables
        shelve_file.close()

    def gv(self, variable_name):
        value, found = self.get_variable(variable_name)
        return value

    def get_values_for_tree_variables(self, data_object, tree_variables):
        tupples = []
        found_all = True
        for variable in tree_variables:
            value, found = data_object.get_variable(variable)
            tupples.append([str(variable), value])
            if found == False:
                found_all = False
        return tupples, found_all

    def add_basic_notes(self, notes, status, source_text, matched, index):
        notes.append("source text = " + str(source_text))
        notes.append("index = " + str(index))
        if matched == "False":
            notes.append("Failed to match event in list build")
            status = "Pass"
        return notes, status

    def apply_avaliable_variables(self, latest_avaliable_variables):
        self.avaliable_variables = latest_avaliable_variables

class Output_Make_Folders(Output_Object):

    def __init__(self, index, name):
        Output_Object.__init__(self, index, name)
        self.set_variable("tree", "")
        self.set_variable("tree_variables", [])
        self.set_variable("tree_paths", [])

    def set_tree_variables(self, tree):
        tree_variables = tree_functions.get_variables_from_tree(tree)
        self.set_variable("tree_variables", tree_variables)
        return tree_variables

    def set_path_variables(self, tree):
        path_variables = tree_functions.get_paths_list_from_tree(tree)
        self.set_variable("tree_paths", path_variables)
        return path_variables

    def check_activate(self, tree, tree_root):
        activate = True
        if os.path.exists(tree_root) == False:
            avtivate = False
        if tree_functions.tree_exists(tree) == False:
            avtivate = False
        return activate

    def add_specific_notes(self, notes, status, found_all):
        if found_all == False:
            notes.append("Not all tree variables were created in list build")
            status = "Pass"
        return notes, status

    def setup_process_output(self, data_object_list):
        """ creates a list, process task that has all the data to process this output [name, type, time_added, global_status, [[index, status, notes, v1, v2..], [index, status, notes, v1, v2, ...]]"""
        process_output_name = self.get_output_name()
        process_output_type = "Make_Folders"
        tree_variable_name = self.gv("tree")
        tree_root = tree_functions.get_root_path_from_tree(tree_variable_name)
        time_string = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        global_status = "Ready"
        events = []

        if self.check_activate(tree_variable_name, tree_root) == True:
            tree_variables = self.set_tree_variables(tree_variable_name)
            tree_paths = self.set_path_variables(tree_variable_name)

            for data_object in data_object_list.get_data_objects():
                tupples, found_all = self.get_values_for_tree_variables(data_object, tree_variables)
                source_text, found_source_text = data_object.get_variable('[SOURCE_TEXT]')
                matched, found_matched = data_object.get_variable('[MATCHED]')
                index = data_object.get_index()

                for tree_path in tree_paths:
                    notes = []
                    status = "Ready"
                    notes, status = self.add_basic_notes(notes, status, source_text, matched, index)
                    notes, status = self.add_specific_notes(notes, status, found_all)

                    tree_path = tree_functions.apply_root_path_to_tree_path(tree_variable_name, tree_path)
                    new_path = tree_functions.apply_variables_to_tree_path(tupples, tree_path)
                    events.append([index, status, notes, new_path])
        else:
            global_status = "Pass"

        process_output = [process_output_name, process_output_type, time_string, global_status, events]
        return process_output

class Output_Copy_Folder(Output_Object):

    def __init__(self, index, name):
        Output_Object.__init__(self, index, name)
        self.set_variable("source_variable", "")
        self.set_variable("destination_variable", "")

    def set_source_variable(self, source_variable):
        self.set_variable("source_variable", source_variable)
        return source_variable

    def set_destination_variable(self, destination_variable):
        self.set_variable("source_variable", destination_variable)
        return destination_variable

    def check_activate(self, source_variable, destination_variable):
        activate = True
        return activate

    def add_specific_notes(self, notes, status, found_source, found_destination):
        if found_source == False:
            notes.append("Source variable not in list build")
            status = "Pass"
        if found_destination == False:
            notes.append("destination variable not in list build")
            status = "Pass"
        return notes, status


    def setup_process_output(self, data_object_list):
        """copys a folder to a new location"""
        process_output_name = self.get_output_name()
        process_output_type = "Copy_Folder"
        time_string = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        global_status = "Ready"
        events = []

        source_variable_name = self.gv("source_variable")
        destination_variable_name = self.gv("destination_variable")

        if self.check_activate(source_variable_name, destination_variable_name) == True:
            for data_object in data_object_list.get_data_objects():
                notes = []
                status = "Ready"
                source_text, found_source_text = data_object.get_variable('[SOURCE_TEXT]')
                matched, found_matched = data_object.get_variable('[MATCHED]')
                source, found_source = data_object.get_variable(source_variable_name)
                destination, found_destination = data_object.get_variable(destination_variable_name)
                index = data_object.get_index()

                notes, status = self.add_basic_notes(notes, status, source_text, matched, index)
                notes, status = self.add_specific_notes(notes, status, found_source, found_destination)
                events.append([index, status, notes, source, destination])

            pass

        else:
            global_status = "Pass"

        process_output = [process_output_name, process_output_type, time_string, global_status, events]
        return process_output




