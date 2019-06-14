#!/usr/bin/python3
from googlesearch import search
import pyqrcode
from pyqrcode import QRCode
import os


data=input("Enter string you want to search ....> ")
li=[]

for i in search(data,stop=3):
	li.append(i)
 
print(li)

for i in range(3):
	qr=pyqrcode.create(data[i])
	qr.svg("url"+str(i)+".png",scale=10)
	print(qr.terminal())

os.system("mkdir /var/www/html/qr")
os.system("mv *.png /var/www/html/qr")            
