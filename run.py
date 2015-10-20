
from subprocess import call
from tasks import runMsh
import sys
from celery import group
from data import exists



def splitTasks(angle_start, angle_stop, n_angles, n_nodes , n_levels, speed):
		jobs=[]
        anglediff= (angle_stop-angle_start)/n_angles
        for i in range(n_angles):
                angle=angle_start+anglediff*i
                exist=False
                # CHECK IF ALEADY EXIST
                if(not(exists(angle, n_nodes, n_levels, speed))):
                	jobs.append(runMsh.s(angle , n_nodes , n_levels, speed))
        tasksGroup=group(jobs)
        result = tasksGroup.apply_async()
        #add the evaluated results to the file
