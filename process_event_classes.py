import os
import sys
import process_functions

class Process_structure_object(object):

    def __init__(self, process_name):
        self.process_structure = process_functions.get_processes_from_file(process_functions.get_process_path_from_name(process_name))
        #self.process_types_dictionary = {'Make_Folders': Output_Make_Folders, 'Copy_Tree': Output_Copy_Tree}

    def