import tree_functions
import shelve
import os

class Output_Object_List(object):

    def __init__(self, data_object_list):
        self.data_objects = data_object_list.get_data_objects()
        self.output_object_list = []
        self.output_types_dictionary = {'Make_Folders': Output_Make_Folders, 'Copy_Tree': Output_Copy_Tree}

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
        new_output_object.set_process_name(new_name)
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
        print "saving shelving output list - ", full_filename
        output_object_data_list = []
        for output_object in self.output_object_list:
            data = output_object.get_full_data()
            print "shelving data - ", data
            output_object_data_list.append(data)
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
            current_names.append(object.get_process_name())
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

    def find_output_from_name(self, output_name):
        found_output = False
        for output in self.output_object_list:
            if output.get_output_name() == output_name:
                found_output = filter
        return found_output

    def set_output_variable_from_output_name(self, variable, value, output_name):
        output = self.find_output_from_name(output_name)
        if output != False:
            output.set_variable(variable, value)

    # def get_tupple_from_data_object_list(self, variable1, variable2):
    #     tupples = []
    #     for data_object in self.data_objects:
    #         variable1_value, varible1_found = data_object.get_variable(variable1)
    #         variable2_value, varible2_found = data_object.get_variable(variable2)
    #         tupple = [variable1_value, variable2_value]
    #         tupples.append(tupple)
    #     print tupples
    #     return tupples

    def process_outputs(self):
        for output in self.output_object_list:
            output.process_output(self.data_objects)



class Output_Object(object):

    def __init__(self, index, name):
        self.index = index
        self.variables = []
        self.name = name



    def set_index(self, index):
        self.index = index

    def get_index(self):
        return self.index

    def set_process_name(self, name):
        self.name = name

    def get_process_name(self):
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







class Output_Make_Folders(Output_Object):

    def __init__(self, index, name):
        Output_Object.__init__(self, index, name)
        self.set_variable("tree", "")
        self.set_variable("tree_variables", [])
        self.set_variable("tree_paths", [])

    def set_tree_variables(self, tree):
        self.set_variable("tree_variables", tree_functions.get_variables_from_tree(tree))

    def set_path_variables(self, tree):
        self.set_variable("tree_paths", tree_functions.get_paths_list_from_tree(tree))

    def check_avtivate(self):
        activate = True
        return activate

    def process_output(self, data_objects):
        print "tree_variables --- ", self.gv("tree_variables")
        print "tree_paths --- ", self.gv("tree_paths")


class Output_Copy_Tree(Output_Object):

    def __init__(self, index, name):
        Output_Object.__init__(self, index, name)
        self.set_variable("source_variable", "")
        self.set_variable("destination_variable", "")



# test_outputs_list = Output_Object_List()
# test_outputs_list.create_new_output("Make_Folders")
# test_outputs_list.create_new_output("Copy_Tree")
# testfile = tree_functions.ROOT_DIR + "/test_shelf"
# test_outputs_list.shelve_output_list_as_file(testfile)
# test_outputs_list.temp_print_output_data()
# test_outputs_list.load_output_list_from_file(testfile)
# test_outputs_list.temp_print_output_data()



