#!/usr/bin/env python
 
import os
import sys
 

def mapper(stdin):
    for line in stdin:
        data = line.split(',')
 
        # perform some error checking
        if len(data) < 4:
            continue
 
        # unpack data
        salary = int(data[3])
        name = data[0]
 
    
        yield "%06d,%s" % (salary, name)

if __name__ == '__main__':
    for output in mapper(sys.stdin):
        print output