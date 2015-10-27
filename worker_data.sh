#!/bin/sh
git clone https://github.com/akilawi/naca_airfoil.git
mv naca_airfoil /home/ubuntu/
cd /home/ubuntu/naca_airfoil
ip_file=$(head -n 1 ip_number.txt)
export BROKERIP=$ip_file
pip install celery
sudo pip install python-novaclient
mkdir /home/ubuntu/naca_airfoil/geo
mkdir /home/ubuntu/naca_airfoil/msh
mkdir /home/ubuntu/naca_airfoil/xml
chmod -R 777 /home/ubuntu/naca_airfoil
sudo -H -u ubuntu bash -c "celery worker -A tasks &"