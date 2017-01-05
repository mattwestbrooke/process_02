class Ouput_Object_List(object):

    def __init__(self):
        self.output_object_list = []

    def add_new_object(self, new_output_object):
        new_output_object.set_index(self.get_next_index())
        self.output_object_list.append(new_output_object)

    def get_next_index(self):
        length = len(self.output_object_list)
        return length

class Output_Object(object):

    def __init__(self):
        self.index = 0
        self.variables = []
        self.name = ""

    def set_index(self, index):
        self.index = index

    def get_index(self):
        return self.index

    def set_process_name(self, name):
        self.name = name

    def get_process_name(self):
        return self.name

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
        return [self.index, self.name, self.variables]

    def set_full_data(self, index, name, variables):
        self.index = index
        self.name = name,
        self.variables = variables



class Output_Make_Folders(Output_Object):

    def __init__(self):
        self.set_variable("tree", "")
        self.set_variable("key", "")


class Output_Copy_Tree(Output_Object):

    def __init__(self):
        self.set_variable("source_variable", "")
        self.set_variable("destination_variable", "")







