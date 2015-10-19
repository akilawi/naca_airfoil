
from subprocess import call
from tasks import runMsh
import sys

TASK_QUEUE=[]
def splitTasks(angle_start, angle_stop, n_angles, n_nodes , n_levels, speed):
        anglediff= (angle_stop-angle_start)/n_angles
        for i in range(n_angles):
                angle=angle_start+anglediff*i
                exist=False
                # CHECK IF ALEADY EXIST

                if(not(exit)):
                	TASK_QUEUE.append(runMsh.delay(angle , n_nodes , n_levels, speed))
                
