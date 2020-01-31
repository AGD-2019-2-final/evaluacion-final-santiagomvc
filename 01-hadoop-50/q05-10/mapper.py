#!/usr/bin/env python
import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
import sys
if __name__ == "__main__":
    for line in sys.stdin:
      line = line[:-1]
      columna = line.split( )[0]
      columna2 =line.split('-')[1]
      sys.stdout.write("{}\t1\n".format(columna2))