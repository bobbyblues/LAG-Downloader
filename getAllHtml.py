# Script to download episodes from Les autres gens (www.lesautresgens.com) in batch
# Save the html pages of all the episodes you want to download in a directory containing this script and getEpisode.py
# Then simply run 'python gettAllHtml.py'
# This will download each episode, store them in a .cbz archive and 

import os
import re
import subprocess

for filename in os.listdir('.'):
	if filename.split('.')[-1] == "html":
		command = ["python", "getEpisode.py", filename]
		subprocess.call(command)
		os.remove(filename)