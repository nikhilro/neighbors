import argparse
import sys
import os
from pprint import pprint
import yaml
import math

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Find your neighbors.')
    parser.add_argument(
        '--input', 
        '-i',
        type=str,
        help='Path to the input file.',
        required=True,
    )
    parser.add_argument(
        '--output',
        '-o',
        default='output.txt',
        type=str,
        help='Path to the output file (appends if already exists)',
    )
    parser.add_argument(
        '--coordinates',
        '-c',
        nargs=2,
        type=float,
        help='The coordinates to your location',
        required=True,
    )

    parsed_args = parser.parse_args()
    if not os.path.exists(parsed_args.input):
        raise RuntimeError(
            # f"The specified input file {parsed_args.input} does not exist."
        )
    
    customers = []
    with open(parsed_args.input) as f:
        for line in f: 
            customers.append(yaml.safe_load(line))
    
    x, y = parsed_args.coordinates
    x, y = math.radians(x), math.radians(y)
    neighouring_customers = []
    for customer in customers:
        xx = math.radians(float(customer['latitude']))
        yy = math.radians(float(customer['longitude']))
        central_angle = math.acos(
            math.sin(x) * math.sin(xx) + 
            math.cos(x) * math.cos(xx) * math.cos(abs(y - yy))
        ) 
        arc_length = 6378.1370 * central_angle # km
        if arc_length < 100:
            neighouring_customers.append((customer['user_id'], customer['name']))


    pprint(neighouring_customers)
    