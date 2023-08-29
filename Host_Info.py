import ipaddress
import os


print("################################")
print("Gathering Host Network Details")
h_ipconfig = os.popen("ipconfig /all").read().strip()
data = h_ipconfig.split("\n")
keywords = ["Subnet", "IPv4", "Host Name", "Default Gateway", "DHCP Server", "DNS Servers", "Domain"]

IPv4 = ""
Subnet = ""

for i in data:
    if any(s in i for s in keywords):
        if "IPv4" in i:
            i = i.replace("(Preferred)", "")
            IPv4 = ((i.split(": ", 1))[1])

        if "Subnet" in i:
            Subnet = ((i.split(": ", 1))[1])
            print(i)

        else:
            print(i)
print("################################")

IPv4 = IPv4.replace(" ", "")
net = ipaddress.ip_network(f"{IPv4}/{Subnet}", strict=False)
print(net)


