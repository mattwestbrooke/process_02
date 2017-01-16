import data_object_classes
import output_object_classes
import process_event_classes
import tree_functions
import defaults










### Test functions ....

test_data_object_list = data_object_classes.Data_Object_List()
test_data_object_list.create_new_data_object_and_set_variables(0, [["[SOURCE_TEXT]", "AVE_101_SC020_SH005"],["[MATCHED]", "True"],["[sceneX]", "020"],["[shotX]", "005"], ["[rootX]", "/Users/MVFX/PycharmTests/root1/VFX_Projects/AVE/shots/101"], ["[sourceX]", "/Users/MVFX/PycharmTests/root1/tests/bob"]])
test_data_object_list.create_new_data_object_and_set_variables(1, [["[SOURCE_TEXT]", "AVE_101_SC010_SH006"],["[MATCHED]", "True"],["[sceneX]", "010"],["[shotX]", "006"], ["[rootX]", "/Users/MVFX/PycharmTests/root1/VFX_Projects/AVE/shots/101"], ["[sourceX]", "/Users/MVFX/PycharmTests/root1/tests/bob"]])
test_data_object_list.create_new_data_object_and_set_variables(2, [["[SOURCE_TEXT]", "AVE_101_SC070_SH007"],["[MATCHED]", "True"],["[sceneX]", "070"],["[shotX]", "007"], ["[rootX]", "/Users/MVFX/PycharmTests/root1/VFX_Projects/AVE/shots/101"], ["[sourceX]", "/Users/MVFX/PycharmTests/root1/tests/bob"]])
test_data_object_list.create_new_data_object_and_set_variables(3, [["[SOURCE_TEXT]", "AVE_101_SC060_008"],["[MATCHED]", "False"],["[sceneX]", "060"],["[shotX]", "022"], ["[rootX]", "/Users/MVFX/PycharmTests/root1/VFX_Projects/AVE/shots/101"], ["[sourceX]", "/Users/MVFX/PycharmTests/root1/tests/bob"]])
test_data_object_list.temp_print_data_objects()

testfile = tree_functions.ROOT_DIR + "/test_data"
test_data_object_list.shelve_data_object_list_as_file(testfile)
print "cleared"
test_data_object_list.clear_data()

test_data_object_list.temp_print_data_objects()
test_data_object_list.load_data_list_from_file(testfile)
print "loaded -- "
test_data_object_list.temp_print_data_objects()

test_data_object_list.filter_object_list.create_new_filter("Key_Filter")
print "our filters ... "
test_data_object_list.filter_object_list.temp_print_filter_data()
test_data_object_list.filter_object_list.set_filter_variable_from_variable_name("key_filter", "MVFX_shot_key", "Key_Filter-1")
test_data_object_list.filter_object_list.set_filter_variable_from_variable_name("active_variable", "[SOURCE_TEXT]", "Key_Filter-1")

test_data_object_list.filter_object_list.create_new_filter("Combine_Filter")
test_data_object_list.filter_object_list.set_filter_variable_from_variable_name("variable_1", "[rootX]", "Combine_Filter-1")
test_data_object_list.filter_object_list.set_filter_variable_from_variable_name("text_2", "/", "Combine_Filter-1")
test_data_object_list.filter_object_list.set_filter_variable_from_variable_name("variable_2", "[sceneX]", "Combine_Filter-1")
test_data_object_list.filter_object_list.set_filter_variable_from_variable_name("text_2", "/", "Combine_Filter-1")
test_data_object_list.filter_object_list.set_filter_variable_from_variable_name("variable_3", "[shotX]", "Combine_Filter-1")
test_data_object_list.filter_object_list.set_filter_variable_from_variable_name("text_3", "/", "Combine_Filter-1")
test_data_object_list.filter_object_list.set_filter_variable_from_variable_name("result_variable", "[COMBINED]", "Combine_Filter-1")



test_data_object_list.filter_object_list.temp_print_filter_data()
test_data_object_list.filter_object_list.apply_filters(test_data_object_list.data_object_list)

test_data_object_list.temp_print_data_objects()
#
# ###############################################
#
test_output_object = output_object_classes.Output_Object_List(test_data_object_list)

test_output_object.create_new_output('Make_Folders')
test_output_object.set_output_variable_from_output_name("tree", "Shot", "Make_Folders-1")
tree_variables = tree_functions.get_variables_from_tree("Shot")
tree_paths = tree_functions.get_paths_list_from_tree("Shot")
test_output_object.set_output_variable_from_output_name("tree_variables", tree_variables, "Make_Folders-1")
test_output_object.set_output_variable_from_output_name("tree_paths", tree_paths, "Make_Folders-1")

test_output_object.create_new_output('Copy_Folder')
test_output_object.set_output_variable_from_output_name("source_variable", "[sourceX]", "Copy_Folder-1")
test_output_object.set_output_variable_from_output_name("destination_variable", "[COMBINED]", "Copy_Folder-1")





test_output_object.set_process_data_to_file("test_01")
#print "outputs ---- "
#test_output_object.temp_print_output_data()

################################################

test_process_list = process_event_classes.Process_list()
test_process_list.temp_print_process()

test_process_list.process_events()

test_process_list.temp_print_process()

# print "search found -- "
# next_event = test_process_list.find_next_event_tupple_to_process()
# print next_event
# event = test_process_list.get_event_by_tupple(next_event)
# event.set_status('Done')


# print ""
# print "new status -- "
# test_process_list.temp_print_process()
#
# print "status of event -- ", event.get_status()
# test_process_list.save_all_process_data_list()


