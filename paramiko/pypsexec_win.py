from pypsexec.client import Client
import os
import time
import sys
import paramiko

host = 'the admin/customer IP'
user = 'DOMAIN\username'
passwd = 'password'

c = Client(host, username=user, password=passwd, encrypt=False)
# c = Client(host, username=username, password=password, encrypt=False, port=139)
c.connect()
try:
     c.create_service()
     stdout = c.run_executable("cmd.exe", arguments="iisreset")
finally:
     c.cleanup()
     c.remove_service()
     c.disconnect()

output = []
output = stdout[0].decode("utf-8")
print(output.split("\r\n")[1:3]
# https://mschirbel.medium.com/how-to-run-commands-in-windows-and-linux-servers-using-python-46af13cbca29
