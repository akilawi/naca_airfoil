#!/bin/sh
git clone https://github.com/akilawi/naca_airfoil.git
mv naca_airfoil /home/ubuntu/
mkdir /home/ubuntu/naca_airfoil/geo
mkdir /home/ubuntu/naca_airfoil/msh
mkdir /home/ubuntu/naca_airfoil/xml
pip install Flask
pip install celery
pip install flower -y
sudo pip install python-novaclient
chmod -R 777 /home/ubuntu/naca_airfoil
cd /home/ubuntu/naca_airfoil
instanceip=$(curl -s checkip.dyndns.org | sed -e 's/.*Current IP Address: //' -e 's/<.*$//')
echo $instanceip >ip_number.txt
source sourcefile_lelli.sh
rabbitmqctl add_user group5 group5
rabbitmqctl add_vhost naca
rabbitmqctl set_permissions -p naca group5 ".*" ".*" ".*"
echo 'Init done, starting Flask webserver'
source /home/ubuntu/naca_airfoil/sourcefile_lelli.sh
#cd /home/ubuntu/naca_airfoil/flask
#python web.py &