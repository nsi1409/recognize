import glob
import os

segments = sorted(glob.glob('segment/*'))
for segment in segments:
	print(segment)
	os.system(f'./recognize.sh {segment}')
