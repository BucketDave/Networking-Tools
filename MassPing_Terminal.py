import os

ping_ip = str(input("Enter IP you want to ping: "))
number = input("Number of CMDs you would like to open: ")
intnumber = int(number)

for i in range(intnumber):
    os.system(f"start  cmd /c ping {ping_ip} -t -l 65500")
