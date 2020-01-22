import json 
import os

class JSONWriter:
    def __init__(self, file_path, items):
        self._file_path = file_path
        self._items = items

    def write_items(self, keys=None):
        file_path= self._file_path
        formatted_items = []

        for item in self._items:
            formatted_items.append({k: item[k] for k in (keys or item.keys())})

        if os.path.isfile(file_path) and os.stat(file_path).st_size != 0:
            print(f'Output file: {file_path} is non-empty. Appending.')
        with open(file_path, mode='a') as f:
            json.dump(formatted_items, f, indent=2, sort_keys=True)