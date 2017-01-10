import os
import sys
import datetime
import shelve
import tree_functions

ROOT_DIR = os.path.dirname(sys.modules['__main__'].__file__)



class Filter_Object_List(object):

    def __init__(self):
        self.filter_object_list = []
        self.filter_types_dictionary = {'Key_Filter': Key_Filter, 'Combine_Filter': Combine_Filter}

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

    def apply_filters(self, data_object_list):
        for filter in self.filter_object_list:
            filter.apply_filter(data_object_list)




class Filter_Object(object):

    def __init__(self, index, name):
        self.index = index
        self.name = name
        self.avaliable_variables = []
        self.variables = []


    def set_index(self, index):
        self.index = index

    def get_index(self):
        return self.index

    def set_filter_name(self, name):
        self.name = name

    def get_filter_name(self):
        return self.name

    def get_filter_type(self):
        name_split = self.name.split('-')
        return name_split[0]

    def set_all_variables(self, variables):
        self.variables = variables

    def get_all_variables(self):
        return self.variables

    def set_all_avaliable_variables(self, avaliable_variables):
        self.avaliable_variables = avaliable_variables

    def get_all_avaliable_variables(self):
        return self.avaliable_variables

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


    def get_full_data(self):
        return [self.index, self.name, self.variables, self.avaliable_variables]

    def set_full_data(self, index, name, variables, avaliable_variables):
        self.index = index
        self.name = name
        self.variables = variables
        self.avaliable_variables = avaliable_variables



class Key_Filter(Filter_Object):

    def __init__(self, index, name):
        Filter_Object.__init__(self, index, name)
        self.set_variable("key_filter", "")
        self.set_variable("active_variable", "")

    def set_key_filter(self, key_filter):
        self.set_variable("key_filter", key_filter)

    def set_active_variable(self, variable):
        self.set_variable("active_variable", variable)

    def apply_filter(self, data_object_list):
        for data_object in data_object_list:
            data_object.set_variable("bogus", "ten")
        #return data_object_list

class Combine_Filter(Filter_Object):

    def __init__(self, index, name):
        Filter_Object.__init__(self, index, name)
        self.set_variable("key_filter", "")
        self.set_variable("active_variable", "")



##### FIlTERS FUNCTIONS


def key_filter(self, filter_vars):
    if filter_vars[2] != "not_set" and filter_vars[2] != "not_set":
        fitler_name = filter_vars[0]
        key_name = filter_vars[2]
        with open((ROOT_DIR + '/keys/' + key_name + '.key'), 'r') as f:
            for line in f:
                key_tx = str(line.rstrip())
        variable_name = filter_vars[3]

        for co in self.container_list:
            value, isfound = co.gv(str(variable_name))
            # print value, isfound
            if isfound == True:
                variable_tuples, match_passed = self.get_variables_from_name_string(value, key_tx, "_")
                for vv in variable_tuples:
                    co.sv(vv[0], vv[1])
                    self.add_current_filter_variables(vv[0])
                co.sv('[MATCHED]', str(match_passed))
                self.add_current_filter_variables('[MATCHED]')


def combine_filter(self, filter_vars):
    print "in combine filter"
    t1 = filter_vars[2]
    v1 = filter_vars[3]
    t2 = filter_vars[4]
    v2 = filter_vars[5]
    t3 = filter_vars[6]
    v3 = filter_vars[7]
    new_name = filter_vars[8]
    if new_name in self.current_filter_variables:
        ok_new = False
        counter = 2
        while ok_new != True:
            try_name = new_name + "-" + str(counter)
            if try_name not in self.current_filter_variables:
                new_v_name = try_name
                ok_new = True
            counter = counter + 1
    else:
        new_v_name = new_name

    print "-- new name - ", new_name
    for co in self.container_list:
        out_val = ""
        if t1 != 'not_set':
            out_val += t1
        if v1 != 'not_set':
            v1_val, v1_f = co.gv(v1)
            if v1_f == True:
                out_val += v1_val
        if t2 != 'not_set':
            out_val += t2
        if v2 != 'not_set':
            v2_val, v2_f = co.gv(v2)
            if v2_f == True:
                out_val += v2_val
        if t3 != 'not_set':
            out_val += t3
        if v3 != 'not_set':
            v3_val, v3_f = co.gv(v3)
            if v3_f == True:
                out_val += v3_val
        co.sv(new_v_name, out_val)
        self.add_current_filter_variables(new_v_name)


def add_filter(self, filter_vars):
    name_1 = filter_vars[0]
    aval_vars = filter_vars[1]
    var_2 = filter_vars[2]
    new_var_3 = filter_vars[3]

    for co in self.container_list:
        if var_2 != 'not_set':
            var2_val, var2_f = co.gv(var_2)
            if var2_f == True:
                co.sv(var_2, (var2_val + new_var_3))


def date_filter(self, filter_vars):
    print "do the date!! - ", filter_vars
    now = datetime.datetime.now()
    new_var = "[DATE_TIME]"
    time_filters = filter_vars[2]
    time_string = now.strftime(time_filters)
    print "time -- ", time_string
    for co in self.container_list:
        co.sv(new_var, time_string)
        self.add_current_filter_variables(new_var)


def tree_filter(self, filter_vars):
    print "processing tree filter"
    tree = filter_vars[2]
    path_key = filter_vars[3]
    new_variable_name = filter_vars[4]
    tree_file_root = ROOT_DIR + '/trees/' + tree + '.root'
    cur_vars = self.current_filter_variables
    # print "@#@@#@ - ", cur_vars
    with open(tree_file_root, 'r') as f:
        for line in f:
            tree_root = str(line.rstrip())
    for co in self.container_list:
        path_key = filter_vars[3]
        if tree_root != "":
            new_key = path_key.replace('[root]', tree_root)
            path_key = new_key
            for var in cur_vars:
                val, found = co.gv(var)
                if found == True:
                    new_key = path_key.replace(var, val)
                    path_key = new_key
        co.sv(new_variable_name, path_key)
        self.add_current_filter_variables(new_variable_name)


def split_filter(self, filter_vars):
    print "in split filter"
    source_var = filter_vars[2]
    split_char = filter_vars[3]
    split_type = filter_vars[4]
    new_var_name = filter_vars[5]

    for co in self.container_list:

        source_string, found = co.gv(source_var)
        if found == True:
            if split_type == "all":
                source_string_split = source_string.split(split_char)
                count = 1
                for ii in source_string_split:
                    var_name = new_var_name + '-' + str(count)
                    var_data = ii
                    co.sv(var_name, var_data)
                    self.add_current_filter_variables(var_name)
                    count = count + 1
            elif split_type == "first":
                source_string_split = source_string.split(split_char)
                var_first = source_string_split[0]
                var_rest = []
                length = len(source_string_split)
                if length >= 2:
                    var_rest.append(source_string_split[1])
                    for jj in range(2, length):
                        var_rest.append(split_char)
                        var_rest.append(source_string_split[jj])
                    var_rest_str = ""
                    for kk in var_rest:
                        var_rest_str = var_rest_str + kk
                    co.sv((new_var_name + "-1"), var_first)
                    self.add_current_filter_variables((new_var_name + "-1"))
                    co.sv((new_var_name + "-2"), var_rest_str)
                    self.add_current_filter_variables((new_var_name + "-2"))
                else:
                    co.sv((new_var_name), source_string_split[0])
                    self.add_current_filter_variables((new_var_name))
            elif split_type == "last":
                source_string_split = source_string.split(split_char)
                var_last = source_string_split[-1]
                var_rest = []
                length = len(source_string_split)
                if length >= 2:
                    var_rest.append(source_string_split[0])
                    for jj in range(1, (length - 1)):
                        var_rest.append(split_char)
                        var_rest.append(source_string_split[jj])
                    var_rest_str = ""
                    for kk in var_rest:
                        var_rest_str = var_rest_str + kk
                    co.sv((new_var_name + "-1"), var_rest_str)
                    self.add_current_filter_variables((new_var_name + "-1"))
                    co.sv((new_var_name + "-2"), var_last)
                    self.add_current_filter_variables((new_var_name + "-2"))
                else:
                    co.sv((new_var_name), source_string_split[0])
                    self.add_current_filter_variables((new_var_name))