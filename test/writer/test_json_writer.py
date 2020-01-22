import unittest
import tempfile

from neighbors.writer.json_writer import JSONWriter

class TestJSONWriter(unittest.TestCase):
    def test_basic_json_output(self):
        with tempfile.NamedTemporaryFile(mode="w+") as f:
            items = [{}, {}]
            items[0]['latitude'] = "36.986375"
            items[0]['user_id'] = 12
            items[1]['latitude'] = "35.92893"
            items[1]['user_id'] = 1
            writer = JSONWriter(f.name, items)
            writer.write_items()
            f.file.seek(0)
            self.assertEqual(f.file.read(), (
                '[\n  {\n    "latitude": "36.986375",\n    "user_id": 12\n  }'
                ',\n  {\n    "latitude": "35.92893",\n    "user_id": 1\n  }\n]'
            ))

    def test_formatted_valid_output(self):
        with tempfile.NamedTemporaryFile(mode="w+") as f:
            items = [{}, {}]
            items[0]['latitude'] = "36.986375"
            items[0]['user_id'] = 12
            items[1]['latitude'] = "35.92893"
            items[1]['user_id'] = 1
            writer = JSONWriter(f.name, items)
            writer.write_items(keys=['user_id'])
            f.file.seek(0)
            self.assertEqual(f.file.read(), (
                '[\n  {\n    "user_id": 12\n  },\n  {\n    "user_id": 1\n  }\n]'
            ))

