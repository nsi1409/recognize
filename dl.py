import glob
import sys
import os

if not os.path.exists('fd/'):
	os.mkdir('fd/')
if not os.path.exists('fd/raw/'):
	os.mkdir('fd/raw/')

if len(sys.argv) > 1:
	for i in range(1, len(sys.argv)):
		inpt = sys.argv[i]
		to_shell = f'yt-dlp -x --audio-format mp3 --output "fd/raw/%(uploader)s - %(title)s.%(ext)s" {inpt}'
		os.system(to_shell)
		print(to_shell)

fds = glob.glob('fd/raw/*.mp3')
for fd in fds:
	fd = fd.replace('fd/raw/', '')
	path = f'fd/segment/{fd.split(".")[0]}'
	if not os.path.exists(path):
		os.mkdir(path)
		print(f'ffmpeg -i \"fd/raw/{fd}\" -f segment -segment_time 8 -c copy \"{path}/slice%04d.mp3\"')
		os.system(f'ffmpeg -i \"fd/raw/{fd}\" -f segment -segment_time 8 -c copy \"{path}/slice%04d.mp3\"')

os.system('python master.py')
