#!/usr/bin/env python
import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
if __name__ == '__main__':
    curkey = None
    for line in sys.stdin:
        key, val = line.split("\t")
        sys.stdout.write("{}".format(val))    
