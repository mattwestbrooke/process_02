import tree_functions
import shelve
import os
import filter_object_classes as foc

class Data_Object_List(object):

    def __init__(self):
        self.data_object_list = []
        self.filter_object_list = []
        self.filter_types_dictionary = {'Key_Filter': foc.Key_Filter, 'Combine_Filter': foc.Combine_Filter}

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
        print "saving - shelving data object list - ", full_filename
        data_object_data_list = []
        for data_object in self.data_object_list:
            data = data_object.get_full_data()
            print "shelving data - ", data
            data_object_data_list.append(data)
        shelve_file = shelve.open(full_filename)
        shelve_file['data_object_list'] = data_object_data_list
        shelve_file.close()

    def load_data_list_from_file(self, full_filename):
        print "loading shelved data list - ", full_filename
        self.data_object_list = []
        shelve_file = shelve.open(full_filename)
        data_object_data_list = shelve_file['data_object_list']
        shelve_file.close()
        for data in data_object_data_list:
            self.create_new_data_object_and_set_variables(data[0], data[1])

    def clear_data(self):
        self.data_object_list = []

    #################


    def create_new_filter(self, filter_type):
        """makes new filter no data just from type"""
        new_filter_index = self.get_next_filter_index()
        new_filter_name = self.get_new_filter_name(filter_type)
        new_filter_object = self.filter_types_dictionary[filter_type](new_filter_index, new_filter_name)
        self.add_new_filter_to_filter_list(new_filter_object)

    def create_new_filter_apply_data(self, filter_type, data):
        """ makes a new filter object from shelved data
        data example - [0, 'Make_Folders-1', [['tree', '']]] ... [index, name, [variables, ..]]
        """
        new_filter_index = self.get_next_filter_index()
        new_filter_name = data[1]
        new_variables = data[2]
        new_available_variables = data[3]
        new_filter_object = self.filter_types_dictionary[filter_type](new_filter_index, new_filter_name)
        new_filter_object.set_process_name(new_filter_name)
        new_filter_object.set_all_variables(new_variables)
        new_filter_object.set_all_avaiable_variables(new_available_variables)
        self.add_new_filter_to_filter_list(new_filter_object)

    def temp_print_filter_data(self):
        print "current object data -"
        for obj in self.filter_object_list:
            print str(obj.get_full_data())

    def add_new_filter_to_filter_list(self, new_filter_object):
        new_filter_object.set_index(self.get_next_filter_index())
        self.filter_object_list.append(new_filter_object)

    def get_next_filter_index(self):
        length = len(self.filter_object_list)
        return length

    def shelve_filter_list_as_file(self, full_filename):
        print "saving shelving filter list - ", full_filename
        filter_object_data_list = []
        for filter_object in self.filter_object_list:
            data = filter_object.get_full_data()
            print "shelving data - ", data
            filter_object_data_list.append(data)
        shelve_file = shelve.open(full_filename)
        shelve_file['filter_object_list'] = filter_object_data_list
        shelve_file.close()

    def load_filter_list_from_file(self, full_filename):
        print "loading shelved filter list - ", full_filename
        self.filter_object_list = []
        shelve_file = shelve.open(full_filename)
        filter_object_data_list = shelve_file['filter_object_list']
        shelve_file.close()
        for data in filter_object_data_list:
            type = self.get_filter_type_from_name(data[1])
            self.create_new_filter_apply_data(type, data)


    def get_filter_type_from_name(self, name):
        name_split = name.split('-')
        return name_split[0]


    def get_all_current_filter_names(self):
        current_filter_names = []
        for filter in self.filter_object_list:
            current_filter_names.append(object.get_filter_name())
        return current_filter_names

    def get_new_filter_name(self, filter_type):
        current_filter_names = self.get_all_current_filter_names()
        counter = 1
        ok_new = False
        while ok_new != True:
            try_name = filter_type + "-" + str(counter)
            if try_name not in current_filter_names:
                new_name = try_name
                ok_new = True
            counter = counter + 1
        return new_name


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




test_data_object_list = Data_Object_List()
test_data_object_list.create_new_data_object_and_set_variables(0, [["source_media", "alpha"],["shot", "010"],["scene", "022"]])
test_data_object_list.create_new_data_object_and_set_variables(1, [["source_media", "beta"],["shot", "020"],["scene", "022"]])
test_data_object_list.create_new_data_object_and_set_variables(2, [["source_media", "gama"],["shot", "030"],["scene", "022"]])
test_data_object_list.create_new_data_object_and_set_variables(3, [["source_media", "delta"],["shot", "040"],["scene", "022"]])
test_data_object_list.create_new_data_object()
test_data_object_list.temp_print_data_objects()

testfile = tree_functions.ROOT_DIR + "/test_data"
test_data_object_list.shelve_data_object_list_as_file(testfile)
print "cleared"
test_data_object_list.clear_data()

test_data_object_list.temp_print_data_objects()
test_data_object_list.load_data_list_from_file(testfile)
print "loaded -- "
test_data_object_list.temp_print_data_objects()

test_data_object_list.create_new_filter("Key_Filter")
test_data_object_list.temp_print_filter_data()
test_data_object_list.filter_object_list[0].apply_filter(test_data_object_list.data_object_list)




