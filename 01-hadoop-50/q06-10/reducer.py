#!/usr/bin/env python
import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
if __name__ == '__main__':
    curkey = None
    total1 = 0
    total2 = 0
    for line in sys.stdin:
        key, val = line.split("\t")
        #val = int(val)
        if total2 == None:
          total1 = val
          total2 = val
        if key == curkey:
            total1 = max(val,total1)
            total2 = min(val,total2)
        else:
             if curkey is not None:
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, total1, total2))
             curkey = key
             total1 = val
             total2 = val 
    sys.stdout.write("{}\t{}\t{}\n".format(curkey, total1, total2))  