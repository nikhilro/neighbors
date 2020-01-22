import unittest

from neighbors.cli.generator import CLIGenerator

class TestCLIGenerator(unittest.TestCase):
    def test_missing_input(self):
        cli = CLIGenerator()
        with self.assertRaises(SystemExit):
            cli._parser.parse_args([])