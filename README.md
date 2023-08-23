# CSGO_Demo_Parser

## This is a simple demo parser script (CSGO_Demo_Parser.py) using [awpy](https://github.com/pnxenopoulos/awpy).
- User needs to change the file path in the `config.ini` file to your own file path containing CSGO demos.
- Demo parsing takes a few seconds per demo, so be patient!
- The result will be a directory `ParsedReplays` that houses the .json file(s).
- From there you will be able to use that data in whatever way you choose.
  
## Features:
- Creates the `ParsedReplays` directory if it doesn't exist within the script directory.
- Ignores all file extensions except for `.dem`.
- Will only parse demos that have not been parsed yet (ones that aren't found in the `ParsedReplays` directory).
- Demo class that you can use to create demo instances with the demo filename
