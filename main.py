"""
Connect to Orion API to update Hudu Documentation Platform via API
"""

import json
import requests
import urllib3
from orionsdk import SwisClient

urllib3.disable_warnings()

user, password =

npm_server = 'orionnpm'
username = 'Nathan'
password = 'Trebnm0233!'

verify = False


swis = SwisClient(npm_server, username, password)

# Get DHCP Network
query = "SELECT Comments AS Name, Address, FoundCIDR as CIDR, VLAN, PercentUsed AS DHCPPercUsed, UsedCount, " \
        "AvailableCount, TotalCount FROM IPAM.DhcpScope WHERE Comments IS NOT NULL AND PercentUsed <> 0"
dhcp_network = swis.query(query)

# Dump output to JSON file with indent = 4
with open('dhcp_network.json', 'w') as f:
    json.dump(dhcp_network, f, indent=4)
