#!/usr/bin/python

import subprocess
import time
import statistics

proc = subprocess.Popen("~/polybar-scripts/info-hackspeed.sh", shell=True, stdout=subprocess.PIPE)

value_list = []
refresh_minutes = 10

while proc.poll() is None:
	refresh = time.time() + 60 * refresh_minutes
	last_refresh = time.strftime("[ LR: %H:%M ⌨ ", time.gmtime())
	while time.time() < refresh:
		output = proc.stdout.readline()
		output = output[:-1]
		value_list.append(int(output))
		print(last_refresh+str(int(statistics.mean(value_list)))+" ]", flush=True)
	value_list = []
