import glob
import json
from subprocess import run
import pprint
import datetime

pp = pprint.PrettyPrinter(indent=4)
segments = sorted(glob.glob('segment/*'))
segment_size = 8
collect = []
parsed = {}
i = 0
for segment in segments:
	print(segment)
	while(True):
		try:
			pd = run(['./recognize.sh', segment], capture_output=True)
			data = json.loads(pd.stdout.decode())
			break
		except:
			print('failed inference')
	collect.append(data)
	try:
		title = data['track']['title']
		artist = data['track']['subtitle']
		song_id = f'{artist} - {title}'
		time_stamp = segment_size*i
		if song_id in parsed:
			parsed[song_id].append(time_stamp)
		else:
			parsed[song_id] = [time_stamp]
	except:
		print('not found')
	i += 1

#pp.pprint(parsed)

outp = {}
for found in parsed:
	if len(parsed[found]) >= 3:
		outp[str(datetime.timedelta(seconds=parsed[found][0]))] = found

pp.pprint(outp)
