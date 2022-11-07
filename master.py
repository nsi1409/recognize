import glob
import json
from subprocess import run
import pprint

pp = pprint.PrettyPrinter(indent=4)
segments = sorted(glob.glob('segment/*'))
segment_size = 8
collect = []
parsed = []
i = 0
for segment in segments:
	print(segment)
	pd = run(['./recognize.sh', segment], capture_output=True)
	data = json.loads(pd.stdout.decode())
	collect.append(data)
	try:
		title = data['track']['title']
		artist = data['track']['subtitle']
		parsed.append((segment_size*i, f'{artist} - {title}'))
	except:
		print('not found')
	if i >= 16:
		break
	i += 1

pp.pprint(collect[5])
print(parsed)
