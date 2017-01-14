import os
import sys
import process_functions

ROOT_DIR = process_functions.get_root_path()


class Process_list(object):
    """List of all objects from each of the '.prcs', process files in the process folder"""

    def __init__(self):
        self.process_list = []
        self.initiate_processes()

    def initiate_processes(self):
        process_file_path_list = self.get_process_file_list()
        for file in process_file_path_list:
            process_data = process_functions.get_process_data_from_file(file[0])
            new_process_object = Process_Object(process_data, file[1])
            self.process_list.append(new_process_object)

    def get_process_file_list(self):
        process_name_list = process_functions.get_all_processes()
        process_file_name_list =[]
        for process_name in process_name_list:
            process_file_name_list.append([(ROOT_DIR + "/process/" + process_name) + ".prcs", process_name])
        return process_file_name_list

    def temp_print_process(self):
        for pp in self.process_list:
            pp.print_data()

    def find_next_event_to_process(self):
        process_index = False
        process_object_name = False
        event_index = False
        counter = 0
        found = False
        result = False
        while found == False:
            for process_object in self.process_list:
                process_index = counter
                process_object_list = process_object.process_objects()
                for process_output_object in process_object_list:
                    process_object_name = process_output_object.get_name()
                    event_list = process_output_object.events()
                    for event in event_list:
                        event_index = event.get_index()
                        event_status = event.get_status()
                        if event_status == 'Ready' and found == False:
                            result = [process_index, process_object_name, event_index]
                            found = True
                counter = counter +1
        return result

    def get_event(self, process_index, process_object_name, event_index):
        process = self.process_list[process_index]
        process_output = process.get_process_output(process_object_name)
        event = process_output.get_event(event_index)
        #print "tester -- ", event.get_new_path()
        return event

    def get_event_by_tupple(self, tupple):
        event = self.get_event(tupple[0], tupple[1], tupple[2])
        return event

    def set_event_status(self, event, status):
        event.set_status(status)

    def save_all_process_data_list(self):
        for process in self.process_list:
            process_data = process.get_process_data()
            process_name = process.get_process_name()
            print 'test name - ', process_name
            process_file_path = process_functions.get_process_path_from_name(process_name)
            print 'test_save - ', process_data
            process_functions.set_process_data_to_file(process_file_path, process_data)











class Process_Object(object):
    """Each process_structure is a class representing each '.prcs' file which is a list of actual process Tasks
    data example - [[name, type, time_added, global_status, [[index, status, notes, v1, v2..], [index, status, notes, v1, v2, ...]], ...]
    this is a list of process_outputs, that make up a process
    """

    def __init__(self, process_data, process_name):
        self.process_data = process_data
        self.process_name = process_name
        self.process_output_list = []
        self.initiate_process_objects(process_data)

    def initiate_process_objects(self, process_data):
        for process_output_data in process_data:
            new_process_output = Process_Output_Object(process_output_data)
            self.process_output_list.append(new_process_output)

    def print_data(self):
        print "process_object - ", self.get_process_data()
        for pp in self.process_output_list:
            pp.print_data()

    def get_process_name(self):
        return self.process_name

    def process_objects(self):
        return self.process_output_list

    def get_process_output(self, name):
        for process_output in self.process_output_list:
            if process_output.get_name() == name:
                return process_output

    def get_process_data(self):
        process_data = []
        for process_output in self.process_output_list:
            process_output_data = process_output.get_process_output_data()
            process_data.append(process_output_data)
            return process_data







class Process_Output_Object(object):
    """List of events and assiated variables, each process represents one output from the output class"""


    def __init__(self, process_output_data):
        self.process_output_data = process_output_data
        self.process_output_name = process_output_data[0]
        self.process_output_type = process_output_data[1]
        self.process_output_time_added = process_output_data[2]
        self.process_output_global_status = process_output_data[3]
        self.process_output_event_list_data = process_output_data[4]
        self.event_types_dictionary = {'Make_Folders': Event_Make_Folders, 'Copy_Tree': Event_Copy_Tree}

        self.event_list = []
        self.initiate_events()

    def initiate_events(self):
        new_index = 0
        for event_data in self.process_output_event_list_data:
            event_data[0] = new_index
            new_filter_object = self.event_types_dictionary[self.process_output_type](event_data)
            self.event_list.append(new_filter_object)
            new_index = new_index + 1

    def print_data(self):
        print "   process output object - ", self.get_process_output_data()
        for pp in self.event_list:
            pp.print_data()

    def get_name(self):
        return self.process_output_name

    def events(self):
        return self.event_list

    def get_event(self, index):
        event = self.event_list[index]
        return event

    def get_process_output_data(self):
        event_data = self.get_event_data()
        process_output_data = [self.process_output_name, self.process_output_type, self.process_output_time_added, self.process_output_global_status, event_data]
        return process_output_data

    def get_event_data(self):
        event_data = []
        for event in self.event_list:
            data = event.get_data()
            event_data.append(data)
        return event_data







class Event_Object(object):
    """base class for events """
    def __init__(self, event_data):
        self.event_data = event_data
        self.index = event_data[0]
        self.status = event_data[1]
        self.notes = event_data[2]

    def print_data(self):
        print "      event object - ", self.get_data()

    def get_index(self):
        return self.index

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

    def get_notes(self):
        return self.notes

    def get_data(self):
        base_data = [self.index, self.status, self.notes]
        extra_data = self.get_extra_data()
        return base_data + extra_data





class Event_Make_Folders(Event_Object):

    def __init__(self, event_data):
        Event_Object.__init__(self, event_data)
        self.new_path = event_data[3]

    def get_new_path(self):
        return self.new_path

    def get_extra_data(self):
        return [self.new_path]

class Event_Copy_Tree(Event_Object):

    def __init__(self, event_data):
        Event_Object.__init__(self, event_data)
        self.source = event_data[3]
        self.destination = event_data[4]
