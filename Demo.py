import shutil
from awpy.parser import DemoParser
import os
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

replay_directory = config.get('General', 'CSGO_Replay_Directory')
script_directory = os.path.dirname(os.path.abspath(__file__))
parsed_directory = os.path.join(script_directory, "ParsedReplays")
demo_extension = ".dem"
json_extension = ".json"


class Demo:
    def __init__(self, filename):
        self._filename = filename

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, new_file_name):
        new_replay_path = os.path.join(replay_directory, new_file_name)
        if isinstance(new_file_name, str):
            if os.path.exists(new_replay_path):
                self._filename = new_file_name
            else:
                raise FileNotFoundError("File not found.")
        else:
            raise ValueError("Path must be a string.")

    def parse_demo(self):
        if self._filename.endswith(demo_extension):
            try:
                if not os.path.exists(parsed_directory):
                    os.makedirs(parsed_directory)

                split_file_path = os.path.splitext(self._filename)
                demo_no_ext = split_file_path[0]
                print(split_file_path)

                # create full path of replay file
                replay_path = os.path.join(replay_directory, self._filename)
                replay_json = demo_no_ext + json_extension

                parsed_directory_with_demo = os.path.join(
                    parsed_directory, demo_no_ext + json_extension)

                if not os.path.exists(parsed_directory_with_demo):
                    # create parser for demo file/parse the file to json
                    demo_parser = DemoParser(demofile=replay_path)
                    demo_parser.parse()

                    # move parsed demo to 'ParsedReplays' directory
                    try:
                        shutil.move(replay_json,
                                    parsed_directory)
                        print(
                            f"File '{replay_json}' moved successfully to the ParsedReplays directory.")

                    except (shutil.Error, OSError) as e:
                        print("Error moving the file:", e)
                else:
                    print(
                        "The demo has already been parsed. Check ParsedReplays directory!")
            except OSError as e:
                print("Error accessing directory:", e)
        else:
            print("Demo file must have .dem extension")