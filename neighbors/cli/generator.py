import argparse

class CLIGenerator:
    def __init__(self):
        self._parser = argparse.ArgumentParser(description='Find your neighbors.')
        self._parsed_args = None

    def warmup(self):
        parser = self._parser
        parser.add_argument(
            '--input', 
            '-i',
            type=str,
            metavar='INPUT_FILE',
            help='Path to the input file.',
            dest='input_file_path',
            required=True,
        )
        parser.add_argument(
            '--output',
            '-o',
            default='output.txt',
            type=str,
            metavar='OUTPUT_FILE',
            dest='output_file_path',
            help='Path to the output file (appends if already exists). default "output.txt"',
        )
        parser.add_argument(
            '--coordinates',
            '-c',
            nargs=2,
            type=float,
            metavar=('LATITUDE', 'LONGITUDE'),
            help='Float coordinates to reference location as (latitude, longitude) in degrees',
            required=True,
        )
        self._parsed_args = parser.parse_args()

    @property
    def user_input(self):
        return self._parsed_args


