import os
import sys
import process_functions

class Process_structure_object(object):

    def __init__(self, process_structure_name):
        self.process_structure_file = process_functions.get_process_path_from_name(process_structure_name)
        self.process_structure = process_functions.get_processes_from_file(self.process_file)
        #self.process_types_dictionary = {'Make_Folders': Output_Make_Folders, 'Copy_Tree': Output_Copy_Tree}

    def update_process_file(self):
        process_functions.set_processes_to_file(self.process_file, self.process_structure)

    def get_next_process_event(self):
        new_event = False
        for process in self.process_structure:
            process_name = process[0]
            process_type = process[1]
            event_list = process[3]
            for event in event_list:
                if event[1] == "Ready":
                    new_event = [process_name, process_type, event[0]]
                    break
            if new_event != False:
                break

    def set_process_status_complete(self, process_name):
        for process in self.process_structure:
            if process[0] == process_name:
                pass

