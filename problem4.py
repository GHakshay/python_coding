import subprocess
import os
import crypt
user=input()
if user.isalpha()==True:
  print( "Enter username :" ,user)
else:
  print("Enter correct username")	

 
password="hello"+user
encriptpassword = crypt.crypt(password,"22") 
subprocess.call("useradd -p " + encriptpassword +" "+user, shell=True)
