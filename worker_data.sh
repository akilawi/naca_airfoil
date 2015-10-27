#!/bin/sh
pip install celery
sudo pip install python-novaclient
git clone https://github.com/akilawi/naca_airfoil.git
mv naca_airfoil /home/ubuntu/
mkdir /home/ubuntu/naca_airfoil/geo
mkdir /home/ubuntu/naca_airfoil/msh
mkdir /home/ubuntu/naca_airfoil/xml
chmod -R 777 /home/ubuntu/naca_airfoil
ip_file=$(head -n 1 ip_number.txt)
export BROKER_IP=$ip_file
cd /home/ubuntu/naca_airfoil
sudo -H -u ubuntu bash -c "celery worker -A tasks &"