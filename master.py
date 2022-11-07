import glob
import json
from subprocess import run
import pprint

pp = pprint.PrettyPrinter(indent=4)
segments = sorted(glob.glob('segment/*'))
i = 0
collect = []
for segment in segments:
	print(segment)
	pd = run(['./recognize.sh', segment], capture_output=True)
	data = json.loads(pd.stdout.decode())
	collect.append(data)
	if i > 15:
		break
	i += 1

#pp.pprint(collect[11])
pp.pprint(collect[14]['track'])
title = collect[14]['track']['title']
artist = collect[14]['track']['subtitle']

print(f'{artist} - {title}')
