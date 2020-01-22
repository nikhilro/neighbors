import unittest
import tempfile

from neighbors.reader.yaml_reader import YAMLReader

class TestYAMLReader(unittest.TestCase):
    def test_correct_yaml(self):
        with tempfile.NamedTemporaryFile(mode="w+") as f:
            f.file.write("\n".join([
                '{ latitude: "36.986375", user_id: 12 }',
                '{ latitude: "35.92893", user_id: 1 }'
            ]))
            f.file.seek(0)
            reader = YAMLReader(f.name)
            reader.read_items()
            items = reader.items
            self.assertEqual(items[0]['latitude'], "36.986375")
            self.assertEqual(items[0]['user_id'], 12)
            self.assertEqual(items[1]['latitude'], "35.92893")
            self.assertEqual(items[1]['user_id'], 1)

    def test_invalid_yaml(self):
        with tempfile.NamedTemporaryFile(mode="w+") as f:
            f.file.write("\n".join([
                '{ badkey1: "36.986375", badkey2: 12 }',
            ]))
            f.file.seek(0)
            reader = YAMLReader(f.name)
            reader.read_items()
            items = reader.items
            with self.assertRaises(KeyError):
                items[0]['latitude']


    def test_non_existent_file_error(self):
        with self.assertRaises(RuntimeError):
            reader = YAMLReader('some-nonexistent-file.txt')

