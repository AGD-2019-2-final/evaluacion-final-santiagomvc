#!/usr/bin/env python
import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
if __name__ == "__main__":
    for line in sys.stdin:
        line = line[:-1]
        columna1 = line.split(',')[1]
        columna2 = line
        sys.stdout.write("{}\t{}\n".format(columna1,columna2))