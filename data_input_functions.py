import defaults

ROOT_DIR = defaults.get_root_path()
UI_STATUS = defaults.get_ui_status()

def get_input_list_from_text_file(text_file_path):
    source_texts = []
    with open(text_file_path, 'r') as f:
        for line in f:
            source_texts.append(str(line.rstrip()))
    return source_texts
