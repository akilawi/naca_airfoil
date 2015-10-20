
from subprocess import call
from tasks import runMsh
import sys
from celery import group
from data import *



def splitTasks(angle_start, angle_stop, n_angles, n_nodes , n_levels, speed):
		jobs=[]
		jobsArgs=[]
		finalResults=[]
        anglediff= (angle_stop-angle_start)/n_angles
        for i in range(n_angles):
                angle=angle_start+anglediff*i
                exist=exists(angle, n_nodes, n_levels, speed)
                # CHECK IF ALEADY EXIST
                if(exit==False):
                	tempArgs=[]
                	tempArgs.append(angle)
                	tempArgs.append(n_nodes)
                	tempArgs.append(n_levels)
                	tempArgs.append(speed)
                	jobsArgs.append(tempArgs)
                	jobs.append(runMsh.s(angle , n_nodes , n_levels, speed))
                else:
                	finalResults.append(get(angle, n_nodes, n_levels, speed)))

        tasksGroup=group(jobs)
        result = tasksGroup.apply_async()

        print jobs
        print "executing airfoils"
        while result.ready() != True:
        	pass

        tasksResults=result.get()
        for j in range(len(tasksResults)):
        	save(jobsArgs[j][0], jobsArgs[j][1], jobsArgs[j][2], jobsArgs[j][3], tasksResults[j])
        	finalResults.append(tasksResults[j])
        return tasksResults