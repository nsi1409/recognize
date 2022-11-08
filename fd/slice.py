import glob
import os

fds = glob.glob('*.mp3')
for fd in fds:
	path = f'segment/{fd.split(".")[0]}'
	if not os.path.exists(path):
		os.mkdir(path)
	os.system(f'ffmpeg -i \"{fd}\" -f segment -segment_time 8 -c copy \"{path}/slice%04d.mp3\"')
	print(f'ffmpeg -i \"{fd}\" -f segment -segment_time 8 -c copy \"{path}/slice%04d.mp3\"')
