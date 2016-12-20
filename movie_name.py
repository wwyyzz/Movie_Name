import os

INPUT_DIR = r'Z:\\Westworld.S01.720p.HDTV.x264-Scene\\'

files = os.listdir(INPUT_DIR)

print(files)

for file in files:
    old_file = INPUT_DIR + file
    print(old_file)
    new_name = INPUT_DIR + file[0:16] + file[-4:]
    os.rename(old_file, new_name)

print(files)