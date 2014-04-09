# Script to download episodes from Les autres gens (www.lesautresgens.com)
# How to use:
# - Go to the webpage of the episode you want (for example http://www.lesautresgens.com/spip.php?article50)
# - Save the webpage source code (as test.html for example)
# - Run 'python getEpisode.py test.html'
# This will download all the pages from the episode and store them in a cbz archive
# Of course you need an account on lesautresgens.com to have access to the full episodes
#
# Moreover, when you visit an episode webpage, temporary urls are created for the different images
# So you need to run this script relatively soon after you generate the html code

import sys
import re
import os
import zipfile
import zlib
import urllib
from urllib import request
import shutil

# We get the name of the html or php file 
# corresponding to the webpage of the episode we want
# to download
infile = sys.argv[1]

# We read all the lines of this file
lines = []
with open(infile, 'r') as sources:
	lines = sources.readlines()

title = ""
images = []

# If a line contains an image, we store it in the images array
# If a line contains the title, we store it as wall
for line in lines:
	if re.search('/bd/', line):
		temp = line.split("'")
		if (len(temp)>1):
			images.append(temp[1])
	if re.search('<title>', line):
		title = line.split('>')[1].split('<')[0]

# We print the title
print(title);

# We create a directory with that title, if it doesn't exist already
directory = title
if not os.path.isdir(directory):
	os.mkdir(directory)
# We get the image format for this episode
ext = images[0].split('.')[-1];
# We download each image one by one
i = 1;
for image in images:
	urllib.request.urlretrieve("http://www.lesautresgens.com"+image, directory+"/"+str(i)+"."+ext)
	print("www.lesautresgens.com"+image)
	i = i + 1;

# We compress the directory as a .zip
zf = zipfile.ZipFile(directory + ".zip", mode="w")
for filename in os.listdir(directory):
	zf.write(directory+"/"+filename, compress_type=zipfile.ZIP_DEFLATED)
zf.close()
# We rename the .zip as a .cbz
os.rename(directory+".zip", directory+".cbz")
# We delete the directory with the images
shutil.rmtree(directory)

