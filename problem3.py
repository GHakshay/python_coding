#!/usr/bin/pytho3

adhoc=[1,2,3,1,4,5,66,22,2,6,0,9]
l1=[]
l2=[]

for i in adhoc:
  if i>5:
    l1.append(i)
    print(i)
    
for i in adhoc:
  if i<=2:
    l2.append(i)
    print(i)
    
    
print(l1)
print(l2)


