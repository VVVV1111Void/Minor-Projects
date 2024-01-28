# Library containing the core functions

import ffmpy
import os
from pathlib import Path

# ffmpy is a library that does stuff that ffmpeg
# does pathlib will be used to help standardize
# stuff and check if the directory exists


def convert_dir(directory, target, source):
    true_path = Path(directory)
    source_files = return_files(true_path, source)
    for item in source_files:
        name = item.stem
        file_path = item
        newpath = Path(directory) / Path(f'{name}.{target}')
        if newpath.exists() is False:
            converter = ffmpy.FFmpeg(
                inputs={str(file_path): None},
                outputs={str(newpath): None}
            )
            converter.run()
        else:
            continue
    return 0

# source - the extensions that will be converted
# target - the target file types that will be converted to
# directory - the directory which will be converted
# Returns 0 on Success

# First, it converts the path to a pathlib class
# It runs a for loop for a every file
# We then save the file name (no extensions) in a variable
# using the file name, we prepare a new path for the new filetype in dir
# If it already exists, we pass and move on (prevent duplicates)


def verify_dir(directory) -> bool:
    true_path = Path(directory)
    if true_path.exists() and os.path.exists(true_path):
        return True
    else:
        return False

# Returns true if the directory exists
# Returns false if it is not found


def return_files(directory, extension) -> list:
    file_paths = []
    dir_files = os.listdir(directory)
    for name in dir_files:
        true_file_path = Path(Path(directory) / Path(name))
        if os.path.exists(true_file_path):  # Re-Check
            if true_file_path.suffix == f".{extension}":
                file_paths.append(true_file_path)
            else:
                continue
        else:
            raise Exception(
                'Error. Was a file deleted while the script was running?')
    return file_paths

# Returns all file paths of files which has the extension given.
# First, it runs os.listdir(directory) which returns all files.
# For each file in the directory, it will be checked if it exists
# and has the source extension. eg, a file with .mp3 but the source
# is opus will be ignored.


def verify_ext(extension, supported) -> bool:
    if extension in supported:
        return True
    else:
        return False

# verify if the extensions are supported and exists
