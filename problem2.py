#!/usr/bin/python3

import os
import time
from googlesearch import search
web=input("plz enter topi:" )
url=[]
for i in search(web,stop=10):
  print(i)
  time.sleep(1)
  url.append(i)
print(url)
