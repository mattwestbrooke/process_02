import os
import sys
import shelve
import defaults


ROOT_DIR = defaults.get_root_path()

def get_process_path_from_name(process_name):
    return ROOT_DIR + '/process/' + process_name + '.prcs'

def get_all_processes():
    process = []
    process_path = ROOT_DIR + '/process'
    for file in os.listdir(process_path):
        if file.endswith(".prcs"):
            file_split = file.split('.')
            process.append(file_split[0])
    return process

def get_new_process_name(process_name):
    current_process_structure_names = get_all_processes()
    counter = 1
    ok_new = False
    while ok_new != True:
        try_name = process_name + "-" + str(counter)
        if try_name not in current_process_structure_names:
            new_process_name = try_name
            ok_new = True
        counter = counter + 1
    return new_process_name

def new_process_file(process_name):
    process_path = ROOT_DIR + '/process'
    new_process_file_path = process_path + '/' + process_name + '.prcs'
    shelve_file = shelve.open(new_process_file_path)
    shelve_file.close()
    return new_process_file_path

def set_process_data_to_file(process_file_path, process_data):
    shelve_file = shelve.open(process_file_path)
    shelve_file['process'] = process_data
    shelve_file.close()

def get_process_data_from_file(process_file_path):
    shelve_file = shelve.open(process_file_path)
    process_data = shelve_file['process']
    shelve_file.close()
    return process_data







