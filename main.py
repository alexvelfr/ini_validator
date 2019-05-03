import sys


def validate(file):
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
        print 'Usage: python %s filename' % sys.argv[0]
        exit(1)
    validate(sys.argv[1])
