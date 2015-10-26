
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
	anglediff= (angle_stop-angle_start)/n_angles
	for i in range(n_angles):
		angle=angle_start+anglediff*i
		exist=exists(angle, n_nodes, n_levels, speed)
		print exist
		# CHECK IF ALEADY EXIST
		if(exist==False):
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
	#while (len(jobs)-(NumOfWorkers*3)) > 0 :
		#ip=createWorker()
		#print ip
		#NumOfWorkers+=1
	NumOfWorkers = 2
	result = tasksGroup.apply_async()
	print jobs
	print "executing airfoils"
	# while result.ready() != True:
	#   pass

	tasksResults=result.get()
	for j in range(len(tasksResults)):
		save(jobsArgs[j][0], jobsArgs[j][1], jobsArgs[j][2], jobsArgs[j][3], tasksResults[j])
		finalResults.append({str(jobsArgs[j][0]):tasksResults[j]})
	return finalResults , NumOfWorkers
