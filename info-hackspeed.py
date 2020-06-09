#!/usr/bin/python

import subprocess, time, statistics

proc = subprocess.Popen(
	"~/.config/polybar/scripts/info-avg-hackspeed/info-hackspeed.sh", shell=True, stdout=subprocess.PIPE
)

value_list = []
refresh_minutes = 10

while proc.poll() is None:
	refresh = time.time() + 60 * refresh_minutes
	last_refresh = time.strftime("[ LR: %H:%M ⌨ ", time.localtime())
	while time.time() < refresh:
		output = proc.stdout.readline()
		output = output[:-1]
		value_list.append(int(output))
		print(last_refresh + str(int(statistics.mean(value_list))) + " ]", flush=True)
	value_list = []
