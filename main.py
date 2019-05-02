import sys
from configparser import RawConfigParser, MissingSectionHeaderError, ParsingError, DuplicateOptionError, DuplicateSectionError


def validate(file):
    try:
        f = open(file, 'r')
        data = f.read()
        f.close()
    except:
        print 'File not found'
        exit(1)
    conf_parser = RawConfigParser()
    try:
        conf_parser.read_string(unicode(data))
    except (MissingSectionHeaderError, ParsingError,DuplicateOptionError, DuplicateSectionError):
        print 'Parse error. File not valid'
        exit(1)
    exit(0)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: python3 %s filename' % sys.argv[0]
        exit(1)
    validate(sys.argv[1])
