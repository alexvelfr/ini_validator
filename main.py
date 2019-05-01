import sys
from configparser import RawConfigParser, MissingSectionHeaderError, ParsingError


def validate(file):
    try:
        with open(file, 'r') as f:
            data = f.read()
    except FileNotFoundError:
        print('File not found')
        exit(1)
    conf_parser = RawConfigParser()
    try:
        conf_parser.read_string(data)
    except (MissingSectionHeaderError, ParsingError):
        print('Parse error. File not valid')
        exit(1)
    exit(0)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Usage: python3 {sys.argv[0]} filename')
        exit(1)
    validate(sys.argv[1])
