import glob
import json
from subprocess import run
import os
import pprint
import datetime
import argparse
import tqdm
pp = pprint.PrettyPrinter(indent=4)

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path')
args = parser.parse_args()

paths = glob.glob('fd/segment/*')
if args.path:
	paths = [args.path]
print(paths)

for path in paths:
	print(path)
	path_id = path.split('/')
	check_index = len(path_id)-1
	if path_id[check_index] != '':
		path_id = path_id[check_index]
	else:
		check_index -= 1
		path_id = path_id[check_index]
	segments = sorted(glob.glob(f'{path}/*'))
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

	outp = {}
	for found in parsed:
		if len(parsed[found]) >= 3:
			outp[str(datetime.timedelta(seconds=parsed[found][0]))] = found

	pp.pprint(outp)
	label_location = 'fd/label/'
	if not os.path.exists(label_location):
		os.mkdir(label_location)
	json_outp = json.dumps(outp)
	with open(label_location+path_id+'.json', 'w') as outfile:
		outfile.write(json_outp)
