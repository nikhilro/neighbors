import os

def validate_file_path(file_path):
    if not os.path.isfile(file_path):
        raise RuntimeError(
            f"The specified path {file_path} is not a file."
        )