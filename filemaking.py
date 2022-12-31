#~~~ Pratham-code ~~~
import time
import os

os.system("cls")

a = input("filename\n")

b = input("text\n")

f = open(f"{a}", "a")
f.write(f"{b}\n")
f.close()

print("file is maked ")
time.sleep(1)

