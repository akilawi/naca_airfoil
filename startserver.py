import os
import novaclient.client
import time

config = {'username':os.environ['OS_USERNAME'], 
          'api_key':os.environ['OS_PASSWORD'],
          'project_id':os.environ['OS_TENANT_NAME'],
          'auth_url':os.environ['OS_AUTH_URL'],
           }
from novaclient.client import Client
nc = Client('2',**config)
#
fl = nc.flavors.find(name="m1.medium")
kp = nc.keypairs.find(name="MBP-Lelli")
img = nc.images.find(name="Ubuntu Server 14.04 LTS (Trusty Tahr)")
u_data_file = file("user_data.yml")
u_data = u_data_file.read()


server = nc.servers.create("mysigserver92", img, flavor=fl, key_name=kp.name, userdata=u_data)

print "Server created."
u_data_file.close()

time.sleep(10)

iplist = nc.floating_ips.list()
for ip_obj in iplist:
  if ((getattr(ip_obj, 'instance_id')) == None):
    floating_ip = getattr(ip_obj, 'ip')
    break
  else:
    print "No IP:s available!"

#floating_ip = nc.floating_ips.create(nc.floating_ip_pools.find(name="ext-net").name)
server.add_floating_ip(floating_ip)
print "IP assigned to the instance", nc.servers.ips(server)