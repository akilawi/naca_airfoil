
from subprocess import call
from tasks import runMsh
import sys

def splitTasks(angle_start, angle_stop, n_angles, n_nodes , n_levels, speed):
        anglediff= (angle_stop-angle_start)/n_angles
        for i in range(n_angles):
                angle=angle_start+anglediff*i
                runMsh.delay(angle , n_nodes , n_levels, speed)



if __name__ == "__main__":
   splitTasks(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]),int(sys.argv[6])
