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


try:
    # make a list of only .dem files from the CSGO Replay Directory
    demo_list = [file_name for file_name in os.listdir(
        replay_directory) if file_name.endswith(demo_extension)]

    if demo_list:
        for demo_file in demo_list:
            # create full path of replay file
            replay_path = os.path.join(replay_directory, demo_file)
            # split from extention to be used in file move
            split_file = os.path.splitext(demo_file)
            replay_no_ext = split_file[0]

            parsed_directory_with_demo = os.path.join(
                parsed_directory, replay_no_ext + json_extension)
            # check if file already exists in ParsedDirectory
            if not os.path.exists(parsed_directory_with_demo):
                # create parser for demo file/parse the file to json
                demo_parser = DemoParser(demofile=replay_path)
                demo_parser.parse()

                # move parsed demo to 'ParsedReplays' directory
                try:
                    shutil.move(replay_no_ext + json_extension,
                                parsed_directory)
                    print(f"File '{demo_file}' moved successfully to the ParsedReplays directory.")

                except (shutil.Error, OSError) as e:
                    print("Error moving the file:", e)
            # parsed demo already exists
            else:
                print("The demo has already been parsed. Check ParsedReplays directory!")
except OSError as e:
    print("Error accessing directory:", e)
