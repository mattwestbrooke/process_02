import data_object_classes
import output_object_classes
import process_event_classes
import tree_functions
import setup_object_classes




process_setup = setup_object_classes.Setup_Object("untitled")



### Test functions ....



# def test_setup_data_object_list():
#
#     TS.data_object_list.create_new_data_object_and_set_variables(0, [["[SOURCE_TEXT]", "AVE_101_SC020_SH005"], ["[MATCHED]", "True"], ["[sceneX]", "020"], ["[shotX]", "005"], ["[rootX]", "/Users/MVFX/PycharmTests/root1/VFX_Projects/AVE/shots/101"], ["[sourceX]", "/Users/MVFX/PycharmTests/root1/tests/bob"]])
#     TS.data_object_list.create_new_data_object_and_set_variables(1, [["[SOURCE_TEXT]", "AVE_101_SC010_SH006"], ["[MATCHED]", "True"], ["[sceneX]", "010"], ["[shotX]", "006"], ["[rootX]", "/Users/MVFX/PycharmTests/root1/VFX_Projects/AVE/shots/101"], ["[sourceX]", "/Users/MVFX/PycharmTests/root1/tests/bob"]])
#     TS.data_object_list.create_new_data_object_and_set_variables(2, [["[SOURCE_TEXT]", "AVE_101_SC070_SH007"], ["[MATCHED]", "True"], ["[sceneX]", "070"], ["[shotX]", "007"], ["[rootX]", "/Users/MVFX/PycharmTests/root1/VFX_Projects/AVE/shots/101"], ["[sourceX]", "/Users/MVFX/PycharmTests/root1/tests/bob"]])
#     TS.data_object_list.create_new_data_object_and_set_variables(3, [["[SOURCE_TEXT]", "AVE_101_SC060_008"], ["[MATCHED]", "False"], ["[sceneX]", "060"], ["[shotX]", "022"], ["[rootX]", "/Users/MVFX/PycharmTests/root1/VFX_Projects/AVE/shots/101"], ["[sourceX]", "/Users/MVFX/PycharmTests/root1/tests/bob"]])
#     TS.data_object_list.temp_print_data_objects()
#
#     testfile = tree_functions.ROOT_DIR + "/test_data"
#     TS.data_object_list.shelve_data_object_list_as_file(testfile)
#     print "cleared"
#     TS.data_object_list.clear_data()
#
#     TS.data_object_list.temp_print_data_objects()
#     TS.data_object_list.load_data_list_from_file(testfile)
#     print "loaded -- "
#     TS.data_object_list.temp_print_data_objects()
#
#     TS.data_object_list.filter_object_list.create_new_filter("Key_Filter")
#     print "our filters ... "
#     TS.data_object_list.filter_object_list.temp_print_filter_data()
#     TS.data_object_list.filter_object_list.set_filter_variable_from_variable_name("key_filter", "MVFX_shot_key", "Key_Filter-1")
#     TS.data_object_list.filter_object_list.set_filter_variable_from_variable_name("active_variable", "[SOURCE_TEXT]", "Key_Filter-1")
#
#     TS.data_object_list.filter_object_list.create_new_filter("Combine_Filter")
#     TS.data_object_list.filter_object_list.set_filter_variable_from_variable_name("variable_1", "[rootX]", "Combine_Filter-1")
#     TS.data_object_list.filter_object_list.set_filter_variable_from_variable_name("text_2", "/", "Combine_Filter-1")
#     TS.data_object_list.filter_object_list.set_filter_variable_from_variable_name("variable_2", "[sceneX]", "Combine_Filter-1")
#     TS.data_object_list.filter_object_list.set_filter_variable_from_variable_name("text_2", "/", "Combine_Filter-1")
#     TS.data_object_list.filter_object_list.set_filter_variable_from_variable_name("variable_3", "[shotX]", "Combine_Filter-1")
#     TS.data_object_list.filter_object_list.set_filter_variable_from_variable_name("text_3", "/", "Combine_Filter-1")
#     TS.data_object_list.filter_object_list.set_filter_variable_from_variable_name("result_variable", "[COMBINED]", "Combine_Filter-1")
#
#     TS.data_object_list.filter_object_list.temp_print_filter_data()
#     TS.data_object_list.filter_object_list.apply_filters(TS.data_object_list.data_object_list)
#
#     TS.data_object_list.temp_print_data_objects()
#
# def test_setup_output_objects():
#     TS.save_setup()
#     TS.load_setup("untitled")
#     TS.output_object_list.create_new_output('Make_Folders')
#     TS.output_object_list.set_output_variable_from_output_name("tree", "Shot", "Make_Folders-1")
#     tree_variables = tree_functions.get_variables_from_tree("Shot")
#     tree_paths = tree_functions.get_paths_list_from_tree("Shot")
#     TS.output_object_list.set_output_variable_from_output_name("tree_variables", tree_variables, "Make_Folders-1")
#     TS.output_object_list.set_output_variable_from_output_name("tree_paths", tree_paths, "Make_Folders-1")
#
#     TS.output_object_list.create_new_output('Copy_Folder')
#     TS.output_object_list.set_output_variable_from_output_name("source_variable", "[sourceX]", "Copy_Folder-1")
#     TS.output_object_list.set_output_variable_from_output_name("destination_variable", "[COMBINED]", "Copy_Folder-1")
#
#     TS.output_object_list.set_process_data_to_file("test_01")
#
# def test_process_list():
#     TPL.temp_print_process()
#     TPL.process_events()
#     TPL.save_all_process_data()
#     TPL.temp_print_process()




# TS = setup_object_classes.Setup_Object("temp")
# test_setup_data_object_list()
# test_setup_output_objects()
# TS.save_setup()
# TPL = process_event_classes.Process_list()
# test_process_list()




