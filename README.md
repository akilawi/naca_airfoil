NACA Airfoil
======

In the NACA Airfoil project our task was to design and implement a cloud-based service that provides an interface for calculating how the angle of attack of NACA Airfoils affect the lift- and drag force. The main objective was to make sure that the system responded in a scalable way to user input, only performing calculations that had not already been done and allocating resources accordingly.

## System Design

Without going into details about how the different parts of the system has been implemented the general flow of the system, from user input to receiving the results is described below.

1. User input from the web page is sent to the main server, the master.
2. The master checks in the database if these values have been calculated before or not, if all values already have been calculated the user gets his results directly and the system state returns to zero. Otherwise it continues to 3.
3. Next step is to check if we need to create additional workers or not, this is dependent on two factors. The number of currently existing workers and the amount of work we need to calculate.
4. As soon as we have the right number of workers the jobs are added to the queue and available for the workers to start calculate.
5. As soon as all workers have completed their work, the results is collected and saved to the database.
6. As a final step the calculated values are returned to the user and the system state is returned to zero.

## How to start the system

1. Please, start by running the startserver.py and make sure you have your ssh key in the same directory.
2. Get your public IP and write it in the file called ip_number.txt.
3. Run the script web.py inside of the flask directory to start the server.
4. access the web portal using your local computer and the IP obtained from before and enjoy.



# NOTE

To find more please read this report explaining how to use the platform and some result examples please reffer to [this](https://www.overleaf.com/read/dwttfrqcprrr)
