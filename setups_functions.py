import os
import sys
import defaults
import shelve


ROOT_DIR = defaults.get_root_path()
SETUP_PATH = ROOT_DIR + '/setups'

def new_setup(new_name):
    new_setup_path, can_create = get_setup_path(new_name)
    made_new_file = False
    if can_create == True:
        shelve_file = shelve.open(new_setup_path)
        output_object_data_list = []
        shelve_file['output_object_list'] = output_object_data_list
        filter_object_data_list = []
        shelve_file['filter_object_list'] = filter_object_data_list
        shelve_file['setup_input_type'] = "text_file"
        shelve_file['setup_input_data'] = ["", "", "", ""]
        shelve_file.close()
        made_new_file = True

        shelve_file = shelve.open(new_setup_path)
        print "1 - ", shelve_file['output_object_list']
        print "2 - ", shelve_file['filter_object_list']
        print "3 - ", shelve_file['setup_input_type']
        print "4 - ", shelve_file['setup_input_data']
    return made_new_file

def get_all_setups():
    setups = []
    setups_path = ROOT_DIR + '/setups'
    for file in os.listdir(setups_path):
        if file.endswith(".setp"):
            file_split = file.split('.')
            setups.append(file_split[0])

    return setups

def setup_exists(new_setup):
    current_setups = get_all_setups()
    if new_setup in current_setups:
        found = True
    else:
        found = False
    return found

def save_input_type(setup_path, type):
    shelve_file = shelve.open(setup_path)
    shelve_file['setup_input_type'] = type
    shelve_file.close()

def load_input_type(setup_path):
    shelve_file = shelve.open(setup_path)
    type = shelve_file['setup_input_type']
    shelve_file.close()
    return type

def save_input_data(setup_path, data):
    shelve_file = shelve.open(setup_path)
    shelve_file['setup_input_data'] = data
    shelve_file.close()

def load_input_data(setup_path):
    shelve_file = shelve.open(setup_path)
    data = shelve_file['setup_input_data']
    shelve_file.close()
    return data

def get_setup_path(name):
    setup_path = SETUP_PATH + '/' + name + '.setp'
    can_create = True
    if os.path.exists(setup_path) == True:
        can_create = False
    return setup_path, can_create

def save_setup_to_file(save_setup_path, filter_object_list, output_object_list):
    filter_object_list.shelve_filter_list_as_file(save_setup_path)
    output_object_list.shelve_output_list_as_file(save_setup_path)

def load_file_to_setup(load_setup_path, filter_object_list, output_object_list):
    filter_object_list.shelve_filter_list_as_file(load_setup_path)
    output_object_list.shelve_output_list_as_file(load_setup_path)










