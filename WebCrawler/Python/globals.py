def get_current_path():
    import pathlib
    return pathlib.Path(__file__).parent.resolve()
	
def get_settings_json():
    import files
    import json
    settings=files.read_file(str(get_current_path())+"\settings.txt")
    #print(type(settings))
    return json.loads(settings)