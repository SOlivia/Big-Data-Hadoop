import sys
import os
from faker import Faker
import csv
import random
from threading import Thread, Lock

def generateData(thread_num,lock):
    
    print "starting thread number: " + str(thread_num)
    filename = "data_"+str(thread_num)+".txt"
    fake = Faker() 
    f = open( filename, 'w+b' )
    writer = csv.DictWriter(f, fieldnames=["name", "address", "city", "salary"])
    #f.close()
    size = 1073741824 # 1gb in bytes
    #size = 100000000 #100 MB file 
    while os.path.getsize(filename) < size:
        writer.writerow(  dict( name=fake.name().replace(","," ").replace("\n"," "),
        address=fake.address().replace(",","").replace("\n"," "),
        city=fake.city().replace(",","").replace("\n"," "),
        salary = random.randrange(40000,150000)))
    f.close()
    print "end thread number: " + str(thread_num)

if __name__ == '__main__':
    lock = Lock()
    threads = [Thread(target = generateData, args = (k,lock,)) for k in range(1)]
    
    for x in threads:
        x.start()
    
    for x in threads:
        x.join()
        
    print "Done"
    	       
