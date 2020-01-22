import yaml

from neighbors.util import validate_file_path

class YAMLReader:
    def __init__(self, file_path):
        validate_file_path(file_path)
        self._file_path = file_path
        self._items = None

    def read_items(self):
        items = []
        with open(self._file_path) as f:
            for line in f: 
                items.append(yaml.safe_load(line))
        self._items = items 

    @property
    def items(self):
        return self._items