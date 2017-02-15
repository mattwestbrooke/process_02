import defaults
import shelve
import filter_object_classes


ROOT_DIR = defaults.get_root_path()

class Data_Object_List(object):

    def __init__(self):
        self.data_object_list = []
        self.filter_object_list = filter_object_classes.Filter_Object_List()

    def get_data_objects(self):
        return self.data_object_list

    def create_new_data_object(self):
        """makes new data object with now variables assigned"""
        new_index = self.get_next_index()
        new_data_object = Data_Object(new_index)
        self.add_new_data_object_to_list(new_data_object)

    def create_new_data_object_and_set_variables(self, index, variable_tupples):
        """makes new data object ad assign variables """
        new_index = index
        new_data_object = Data_Object(new_index)
        new_data_object.set_variables(variable_tupples)
        self.add_new_data_object_to_list(new_data_object)

    def temp_print_data_objects(self):
        print "current object data -"
        for obj in self.data_object_list:
            print str(obj.get_full_data())

    def add_new_data_object_to_list(self, new_data_object):
        new_data_object.set_index(self.get_next_index())
        self.data_object_list.append(new_data_object)

    def get_next_index(self):
        length = len(self.data_object_list)
        return length

    def shelve_data_object_list_as_file(self, full_filename):
        #print "saving - shelving data object list - ", full_filename
        data_object_data_list = []
        for data_object in self.data_object_list:
            data = data_object.get_full_data()
            #print "shelving data - ", data
            data_object_data_list.append(data)
        shelve_file = shelve.open(full_filename)
        shelve_file['data_object_list'] = data_object_data_list
        shelve_file.close()

    def load_data_list_from_file(self, full_filename):
        #print "loading shelved data list - ", full_filename
        self.data_object_list = []
        shelve_file = shelve.open(full_filename)
        data_object_data_list = shelve_file['data_object_list']
        shelve_file.close()
        for data in data_object_data_list:
            self.create_new_data_object_and_set_variables(data[0], data[1])

    def setup_data_objects_from_input_list(self, input_list):
        self.clear_data()
        index = 0
        for input_string in input_list:
            self.create_new_data_object_and_set_variables(index, [["[SOURCE_TEXT]", input_string]])
            index = index +1

    def clear_data(self):
        self.data_object_list = []

class Data_Object(object):

    def __init__(self, id):
        self.id = id
        self.variables = []

    def set_index(self, index):
        self.index = index

    def get_index(self):
        return self.index

    def set_variable(self, attribute, value):
        found = False
        for ii in self.variables:
            if ii[0] == attribute:
                ii[1] = value
                found = True

        if found == False:
            self.variables.append([attribute, value])
        return found

    def get_variable(self, attribute):
        found = False
        result = ""
        for jj in self.variables:
            if jj[0] == attribute:
                result = jj[1]
                found = True
        return result, found

    def set_variables(self, variable_tupples):
        for tupple in variable_tupples:
            self.set_variable(tupple[0], tupple[1])

    def get_full_data(self):
        return [self.id, self.variables]

    def get_variable_tupples(self):
        return self.variables







