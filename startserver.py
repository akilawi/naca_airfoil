import os
import novaclient.client
import time
from novaclient.client import Client
  def createServer:
  config = {'username':os.environ['OS_USERNAME'], 
            'api_key':os.environ['OS_PASSWORD'],
            'project_id':os.environ['OS_TENANT_NAME'],
            'auth_url':os.environ['OS_AUTH_URL'],
             }

  nc = Client('2',**config)
  #
  fl = nc.flavors.find(name="m1.medium")
  kp = nc.keypairs.find(name="ahil1")
  img = nc.images.find(name="airfoil-master")
  u_data_file = file("user_data.yml")
  u_data = u_data_file.read()


  server = nc.servers.create("worker", img, flavor=fl, key_name=kp.name, userdata=u_data)

  print "Server created."
  u_data_file.close()

  while server.status == 'BUILD':
      time.sleep(5)
      print('...')
      server = nc.servers.get(server.id)
  print('Server ready')

  iplist = nc.floating_ips.list()
  floating_ip=None
  for ip_obj in iplist:
    if ((getattr(ip_obj, 'instance_id')) == None):
      floating_ip = getattr(ip_obj, 'ip')
      break
    else:
      print "No IP:s available!"
  if floating_ip==None:
  	floating_ip = nc.floating_ips.create(nc.floating_ip_pools.find(name="ext-net").name)
  server.add_floating_ip(floating_ip)
  temp =nc.servers.ips(server)
  print "IP assigned to the instance", temp
  return temp['ACC-Course-net'][1]['addr']


def startWorker(ip):
  

