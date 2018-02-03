import os
from subprocess import Popen, PIPE

for i in range(30):
	p1 = Popen(['perf', 'stat', '-e', 'cache-misses', 'python', 'evaluate_accuracy.py'], stdout=PIPE)
	print p1.communicate()
	#if(output.find("cache-misses",0,len(output)))
	#print output



