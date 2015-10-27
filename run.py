
from subprocess import call
from tasks import runMsh
import sys
from celery import group
from data import *
from startserver import *
import time



def splitTasks(angle_start, angle_stop, n_angles, n_nodes , n_levels, speed , NumOfWorkers):
	jobs=[]
	jobsArgs=[]
	finalResults=[]
	totalWorkItems = 0
	anglediff= (angle_stop-angle_start)/n_angles
	for i in range(n_angles):
		#This calculations might be wrong, does i get 10?
		angle=angle_start+anglediff*i
		exist=exists(angle, n_nodes, n_levels, speed)
		print exist
		# CHECK IF ALEADY EXIST
		if(exist==False):
			totalWorkItems+=1
			tempArgs=[]
			tempArgs.append(angle)
			tempArgs.append(n_nodes)
			tempArgs.append(n_levels)
			tempArgs.append(speed)
			jobsArgs.append(tempArgs)
			jobs.append(runMsh.s(angle , n_nodes , n_levels, speed))
		else:   
			finalResults.append({str(angle):get(angle, n_nodes, n_levels, speed)})
	tasksGroup=group(jobs)


	#Check for workitems and also if we already have workers
	if(totalWorkItems>9 and NumOfWorkers<3):
		print "Spawning 3 workers, total work items = ", totalWorkItems
		for i in range(3-NumOfWorkers):
			ip=createWorker(i)
			print "Worker created, IP: ", ip
		NumOfWorkers = 3
	elif(totalWorkItems>6 and NumOfWorkers<2):
		print "Spawning 2 workers, total work items = ", totalWorkItems
		for i in range(2):
			ip=createWorker(i)
			print "Worker created, IP: ", ip
		NumOfWorkers = 2

	#If first iteration and/or no workers have previously been started
	if (NumOfWorkers<1):
		if(totalWorkItems>9):
			print "Spawning 3 workers, total work items = ", totalWorkItems
			for i in range(3):
				ip=createWorker(i)
				print "Worker created, IP: ", ip
			NumOfWorkers = 3
		elif(totalWorkItems>6):
			print "Spawning 2 workers, total work items = ", totalWorkItems
			for i in range(2):
				ip=createWorker(i)
				print "Worker created, IP: ", ip
			NumOfWorkers = 2
		elif(totalWorkItems>0):
			print "Spawning 1 worker, total work items = ", totalWorkItems
			for i in range(1):
				ip=createWorker(i)
				print "Worker created, IP: ", ip
				NumOfWorkers = 1
		else:
			print "Spawning 0 workers, total work items = ", totalWorkItems
	time.sleep(60)
	print "Done spawning "+ str(NumOfWorkers) +" workers."
	result = tasksGroup.apply_async()
	print "Executing airfoils in queue: ", jobs

	tasksResults=result.get()
	for j in range(len(tasksResults)):
		save(jobsArgs[j][0], jobsArgs[j][1], jobsArgs[j][2], jobsArgs[j][3], tasksResults[j])
		finalResults.append({str(jobsArgs[j][0]):tasksResults[j]})
	return finalResults , NumOfWorkers