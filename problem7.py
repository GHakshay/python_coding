#!/usr/bin/python3




'''file=input("Enter file name you want to create")
f=open(file,"a+")
f.seek(0)
f.close()'''
import datetime

atime={}
curr_time=[]
no_files=int(input("how many files you want to create: " ))
for i in range(no_files):
      file=input("Enter file name you want to create: ")
      f=open(file,"a+")
      curr_time.append(datetime.datetime.now())

      atime[file]=curr_time[i]


print(atime)

answer=input("Do you want to see access time ?yes/no ")
if answer=='yes':
        f_name=input("enter file name: ")
        print(atime[f_name])
else:
  print("ok")
    
