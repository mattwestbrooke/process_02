import data_object_classes
import output_object_classes
import tree_functions








### Test functions ....

test_data_object_list = data_object_classes.Data_Object_List()
test_data_object_list.create_new_data_object_and_set_variables(0, [["source_media", "AVE_101_SC020_SH005"],["shotX", "010"],["sceneX", "022"]])
test_data_object_list.create_new_data_object_and_set_variables(1, [["source_media", "AVE_102_SC010_SH006"],["shotX", "020"],["sceneX", "022"]])
test_data_object_list.create_new_data_object_and_set_variables(2, [["source_media", "AVE_103_SC070_SH007"],["shotX", "030"],["sceneX", "022"]])
test_data_object_list.create_new_data_object_and_set_variables(3, [["source_media", "AVE_104_SC060_SH008"],["shotX", "040"],["sceneX", "022"]])
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
test_data_object_list.filter_object_list.set_filter_variable_from_variable_name("active_variable", "source_media", "Key_Filter-1")

test_data_object_list.filter_object_list.create_new_filter("Combine_Filter")
test_data_object_list.filter_object_list.set_filter_variable_from_variable_name("variable_1", "[PROJECT]", "Combine_Filter-1")
test_data_object_list.filter_object_list.set_filter_variable_from_variable_name("text_2", "___", "Combine_Filter-1")
test_data_object_list.filter_object_list.set_filter_variable_from_variable_name("variable_2", "[SCENE]", "Combine_Filter-1")
test_data_object_list.filter_object_list.set_filter_variable_from_variable_name("result_variable", "[COMBINED]", "Combine_Filter-1")



test_data_object_list.filter_object_list.temp_print_filter_data()
test_data_object_list.filter_object_list.apply_filters(test_data_object_list.data_object_list)

test_data_object_list.temp_print_data_objects()

###############################################

test_output_object = output_object_classes.Output_Object_List(test_data_object_list)
#test_output_object.get_tupple_from_data_object_list('[MATCHED]', '[EPISODE]')
test_output_object.create_new_output('Make_Folders')
test_output_object.set_output_variable_from_output_name("tree", "Shot", "Make_Folders-1")
tree_variables = tree_functions.get_variables_from_tree("Shot")
tree_paths = tree_functions.tree_functions.get_paths_list_from_tree("Shot")
test_output_object.set_output_variable_from_output_name("tree_variables", tree_variables, "Make_Folders-1")
test_output_object.set_output_variable_from_output_name("tree_paths", tree_paths, "Make_Folders-1")


test_output_object.process_outputs()
print "outputs ---- "
test_output_object.temp_print_output_data()