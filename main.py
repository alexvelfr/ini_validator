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


def validate2(file):
    excepted_symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '/', '?', '\\', '"', '\'']
    try:
        f = open(file, 'r')
    except:
        sys.exit(1)
    valid = True
    for line in f.readlines():
        arr_line = line.strip('\n, ').split('=')
        if len(arr_line) == 1:
            if not (arr_line[0].startswith(u'[') and arr_line[0].endswith(u']')):
                valid = False
                break
        elif len(arr_line) > 1:
            for sm in excepted_symbols:
                if sm in arr_line[0]:
                    valid = False
                    break
        else:
            valid = False
            break
    f.close()

    if valid:
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: python3 %s filename' % sys.argv[0]
        exit(1)
    # validate(sys.argv[1])
    validate2(sys.argv[1])
