import glob
import os
import json
from subprocess import run

segments = sorted(glob.glob('segment/*'))
i = 0
collect = []
for segment in segments:
	print(segment)
	pd = run(['./recognize.sh', segment], capture_output=True)
	data = json.loads(pd.stdout.decode())
	collect.append(data)
	if i > 12:
		break
	i += 1

print(collect[11])
