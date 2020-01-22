from operator import itemgetter

from neighbors.cli.generator import CLIGenerator
from neighbors.reader.yaml_reader import YAMLReader
from neighbors.analyzer.orthodormic_analyzer import OrthodermicAnalyzer
from neighbors.writer.json_writer import JSONWriter

if __name__ == "__main__":
    cli = CLIGenerator()
    cli.warmup()
    user_input = cli.user_input
    
    reader = YAMLReader(user_input.input_file_path)
    reader.read_items()
    customers = reader.items
    
    analyzer = OrthodermicAnalyzer(customers, user_input.coordinates)
    analyzer.find_admissible_items()
    neighboring_customers = analyzer.admissible_items

    writer = JSONWriter(user_input.output_file_path, neighboring_customers)
    writer.write_items(keys=('user_id', 'name'), sort=itemgetter('user_id'))

    