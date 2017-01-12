import os
import sys
import shelve

def get_root_path():
    ROOT = os.path.dirname(sys.modules['__main__'].__file__)
    with open((ROOT + '/setups_path'), 'r') as f:
        for line in f:
            ROOT_DIR = str(line.rstrip())
    if ROOT_DIR == "ROOT":
        ROOT_DIR = ROOT
    return ROOT_DIR

ROOT_DIR = get_root_path()

def get_process_path_from_name(process_name):
    return ROOT_DIR + '/process' + process_name + '.prcs'

def get_all_processes():
    processes = []
    process_path = ROOT_DIR + '/process'
    for file in os.listdir(process_path):
        if file.endswith(".prcs"):
            file_split = file.split('.')
            processes.append(file_split[0])
    return processes

def get_new_processes_name(process_name):
    current_process_names = get_all_processes()
    counter = 1
    ok_new = False
    while ok_new != True:
        try_name = process_name + "-" + str(counter)
        if try_name not in current_process_names:
            new_output_name = try_name
            ok_new = True
        counter = counter + 1
    return new_output_name

def new_processes_file(process_name):
    process_path = ROOT_DIR + '/process'
    new_processes_file_path = process_path + '/' + process_name + 'prcs'
    shelve_file = shelve.open(new_processes_file_path)
    shelve_file.close()
    return new_processes_file_path

def set_processes_to_file(processes_file_path, processes_structure):
    shelve_file = shelve.open(processes_file_path)
    shelve_file['process_structure'] = processes_structure
    shelve_file.close()

def get_processes_from_file(processes_file_path):
    shelve_file = shelve.open(processes_file_path)
    process_structure = shelve_file['process_structure']
    shelve_file.close()
    return process_structure

def get_next_process_event(process_structure):
    new_event = False
    for process in process_structure:
        process_name = process[0]
        process_type = process[1]
        event_list = process[3]
        for event in event_list:
            if event[1] == "Ready":
                new_event = [process_name, process_type, event[0]]
                break
        if new_event != False:
            break





