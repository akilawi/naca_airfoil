import os
from novaclient.client import Client
 
config = {'username':os.environ['OS_USERNAME'],
          'api_key':os.environ['OS_PASSWORD'],
          'project_id':os.environ['OS_TENANT_NAME'],
          'auth_url':os.environ['OS_AUTH_URL'],
           }
 
nova = Client('2',**config)
 
instances = nova.servers.findall()
#Todo: Fixa IP
myid = '0c253eef5aed4ee199611a2ad7a5470a'
for a in instances:
    if a.user_id == myid:
        a.delete()