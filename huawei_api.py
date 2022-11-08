from huawei_lte_api.Client import Client
from huawei_lte_api.AuthorizedConnection import AuthorizedConnection
from huawei_lte_api.Connection import Connection

# connection = Connection('http://192.168.8.1/') For limited access, I have valid credentials no need for limited access
# connection = AuthorizedConnection('http://admin:MY_SUPER_TRUPER_PASSWORD@192.168.8.1/', login_on_demand=True) # If you wish to login on demand (when call requires authorization), pass login_on_demand=True

connection = AuthorizedConnection('http://user:password@LTE_ROUTER_IP/')

client = Client(connection) # This just simplifies access to separate API groups, you can use device = Device(connection) if you want

print(client.device.signal())  # Can be accessed without authorization

print(client.device.information())  # Needs valid authorization, will throw exception if invalid credentials are passed in URL

client.device.reboot()
# For more API calls, just look on code in the huawei_lte_api/api folder, there is no separate DOC yet.
# From: https://forum.huawei.com/enterprise/en/forum.php?mod=viewthread&tid=572785&page=1#pid5433294