import os
import sys
import defaults


ROOT_DIR = defaults.get_root_path()
TREE_ROOT_DIR = ROOT_DIR + '/trees/'

def get_all_current_trees():
    trees = []
    trees_path = ROOT_DIR + '/trees'
    for file in os.listdir(trees_path):
        if file.endswith(".tree"):
            file_split = file.split('.')
            trees.append(file_split[0])

    return trees

def get_all_current_keys():
    keys = []
    keys_path = ROOT_DIR + '/keys'
    for file in os.listdir(keys_path):
        if file.endswith(".key"):
            file_split = file.split('.')
            keys.append(file_split[0])

    return keys

def tree_exists(tree):
    current_trees = get_all_current_trees()
    if tree in current_trees:
        found = True
    else:
        found = False
    return found

def get_paths_list_from_tree(tree):
    paths =[]
    tree_file = ROOT_DIR + '/trees/' + tree + '.tree'
    with open(tree_file, 'r') as f:
        for line in f:
            paths.append(str(line.rstrip()))
    return paths

def get_root_path_from_tree(tree):
    tree_file_root = ROOT_DIR + '/trees/' + tree + '.root'
    with open(tree_file_root, 'r') as f:
        for line in f:
            tree_root = str(line.rstrip())
    return tree_root

def get_key_string_from_key_file(key):
    with open((ROOT_DIR + '/keys/' + key + '.key'), 'r') as f:
        for line in f:
            key_string = str(line.rstrip())
    return key_string

def get_variables_from_tree(tree):
    variables = []
    tree_variable_file = ROOT_DIR + '/trees/' + tree + '.varb'
    with open(tree_variable_file, 'r') as f:
        for line in f:
            variables.append(str(line.rstrip()))
    return variables

def get_variables_list_from_key(key_string, split_char):

    """return just the variables from a key string"""

    key_break_list = get_key_break_list(key_string, split_char)
    variables = []
    for ii in key_break_list:
        variables.append(ii[1])

def get_key_break_list(key_string, split_char):

    """ will return a parsed list breaking down the key string into a list eg.
        key_string = "[SHOW]_Sq[SEQUENCE]_Sc[SCENE]_[SHOT]"
        split_char = "_"
        result = [['', '[SHOW]', ''], ['', '[SEQUENCE]', ''], ['', '[SCENE]', ''], ['', '[SHOT]', '']]
    """
    key_string_split = key_string.split(split_char)
    split_num = len(key_string_split)
    break_key_list = []
    for ee in range(0, split_num):
        if "[" in key_string_split[ee] and "]" in key_string_split[ee]:
            bb = []
            cc = key_string_split[ee]
            front_b = (key_string_split[ee].split("["))[0]
            back_b = (key_string_split[ee].split("]"))[-1]
            var_mid = "[" + cc[cc.find("[") + 1:cc.find("]")] + "]"
            bb.append(front_b)
            bb.append(var_mid)
            bb.append(back_b)
        else:
            bb = "[" + key_string_split[ee] + "]"
        break_key_list.append(bb)
    return break_key_list

def get_variable_tupples_from_source_string(source_string, key_string, split_char):

    """ will return a tuple '0' will be alist of variables matched to parts of the source_string, '1' is the bool to state weather the match was successful
        result = ([['[SHOW]', 'AVE'], ['[SEQUENCE]', 'CAB'], ['[SCENE]', '001'], ['[SHOT]', '240']], True)
    """
    key_string_split = get_key_break_list(key_string, split_char)
    name_string_split = source_string.split(split_char)
    key_list_len = len(key_string_split)
    name_list_len = len(name_string_split)

    match_passed = True
    variable_tuples = []

    if name_list_len >= key_list_len:

        for ss in range(0, key_list_len):
            key_string_obj = key_string_split[ss]
            name_string_obj = name_string_split[ss]
            len_key_string_obj = len(key_string_obj)
            len_name_string_obj = len(name_string_obj)

            if len_key_string_obj == 1:
                if key_string_obj != name_string_obj:
                    match_passed = False

            elif len_key_string_obj == 3:
                len_key_string_obj_0 = len(key_string_obj[0])
                for qq in range(0, len_key_string_obj_0):
                    if name_string_obj[0] != key_string_obj[0][qq]:
                        if key_string_obj[0][qq] != "*":
                            match_passed = False
                    name_string_obj = name_string_obj[1:]

                len_key_string_obj_2 = len(key_string_obj[2])
                key_string_obj_2 = key_string_obj[2]
                key_string_obj_rev2 = key_string_obj_2[::-1]
                for ee in range(0, len_key_string_obj_2):
                    if name_string_obj[-1] != key_string_obj_rev2[ee]:
                        if key_string_obj_rev2[ee] != "*":
                            match_passed = False
                    name_string_obj = name_string_obj[:-1]

                var_tupple = [key_string_obj[1], name_string_obj]
                variable_tuples.append(var_tupple)

    else:
        match_passed = False

    return variable_tuples, match_passed

def apply_root_path_to_tree_path(tree, tree_path):
    """" Returns version of tree path with root variable replaced """
    root_path = get_root_path_from_tree(tree)
    new_tree_path = tree_path.replace('[root]', root_path)
    return new_tree_path

def apply_variables_to_tree_path(variable_tupples, tree_path):
    """Returns version of tree path with variables replaced using variable tupples"""
    for ii in variable_tupples:
        new_tree_path = tree_path.replace(ii[0], ii[1])
        tree_path = new_tree_path
    return tree_path

def get_new_tree_variables(new_tree):
    fname = ROOT_DIR + '/trees/' + new_tree + ".tree"
    fname_root = ROOT_DIR + '/trees/' + new_tree + ".root"
    fname_varb = ROOT_DIR + '/trees/' + new_tree + ".varb"
    new_name_ext = new_tree + ".tree"
    new_name = new_tree
    return fname, fname_root, fname_varb, new_name_ext, new_name

def make_new_tree(new_tree):
    new_tree_file = open(TREE_ROOT_DIR + new_tree + '.tree', 'w')
    new_root_file = open(TREE_ROOT_DIR + new_tree + '.root', 'w')
    new_varb_file = open(TREE_ROOT_DIR + new_tree + '.varb', 'w')
    new_tree_file.close()
    new_root_file.close()
    new_varb_file.close()


