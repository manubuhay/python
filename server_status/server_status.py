import subprocess
import os
# import pprint # module to pretty print dictionaries
import json # better at pretty printing dictionaries

status=False
servers=[
    {
    "name": "Zabbix",
    "ip address": "192.168.255.62",
    "operating system": "CentOS",
    "kernel": "Linux",
    "is_online": status
    },
    {
    "name": "Google DNS Server",
    "ip address": "8.8.4.4",
    "operating system": "Ubuntu",
    "kernel": "Linux",
    "is_online": status
    },
    {
    "name": "Windows XP KVM",
    "ip address": "192.168.255.50",
    "operating system": "Windows XP",
    "kernel": "NT",
    "is_online": status
    },
    {
    "name": "Clean Browsing DNS Server",
    "ip address": "185.228.169.9",
    "operating system": "Ubuntu",
    "kernel": "Linux",
    "is_online": status
    }
        ]

# print(servers[0]["online"])
# print(servers[0]["ip address"])

shell_value=False
count = "-c"
if os.name == "nt":
    shell_value=True
    count = "-n"
for i in range(len(servers)):
    print("Pinging: %s"%(servers[i]["name"]))
    results=subprocess.run(["ping",count,"2",servers[i]["ip address"]], shell=shell_value, text=True)
    if results.returncode == 0:
        servers[i]["is_online"] = True

# print(servers)
# for x in servers:
#     print(x)
# pp = pprint.PrettyPrinter(depth=4)
# pp.pprint(servers)
print (json.dumps(servers, indent=4))