

from celery import Celery
app = Celery('tasks', backend='rpc://', broker='amqp://')
def runMsh(angle , n_nodes , n_levels,speed):
        command='bash runfirst.sh %d %d %d %d %d %d' % (angle , angle , 1 , n_nodes , n_levels , spe$
        print call(command, shell=True)








