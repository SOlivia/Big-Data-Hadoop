#!/usr/bin/env python
 
import sys
 
current_salary = None
current_name = ''

def reducer(stdin):
     current_salary = None
     current_name = ''
     for line in stdin:
          data = line.split(',')
          salary = data[0]
          name = data[1].strip()
     
          if current_salary == salary:
               current_name = current_name + ":" + name
          else:
               if current_salary:
                    yield '%s\t%s' % (current_salary, current_name)
               current_salary = salary
               current_name = name

     if current_salary == salary:
          yield '%s\t%s' % (current_salary, current_name)      	    

if __name__ == '__main__':
    for output in reducer(sys.stdin):
        print output