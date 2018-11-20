# Script that sets the ID3 Artist tag in the current directory to the folder name

import os
import sys
from sets import Set
import subprocess

#print "\n".join(sys.argv)

#HTML_Directory = sys.argv[1]
#os.chdir(HTML_Directory)

#Find all HTML files and strore their paths
Files = []
Unique_Bands = Set()
for root, dirs, files in os.walk("."):
	for fil in files:
		if fil.endswith(".mp3"):
			HTML = "".join(root) + "".join(dirs) + "/" + fil
			HTML = os.path.join(root, fil)
			Files.append(HTML)
			#print "file: " + str(fil) + " dir: " + str(root[2:])
			new = ['id3v2','--artist', '"'+str(root[2:])+'"', os.path.join(root, fil)]
			print "file: " + str(fil) + " " + str(new)
			# Call id3v2 to set the Id3 Artist tag to the directory name
			subprocess.check_output(['id3v2','--artist', str(root[2:]), os.path.join(root, fil)])
			#sys.exit()
 			Unique_Bands.add(root[2:])
	#print root, dirs, files

print "Found Unique bands: "
print Unique_Bands

print "Script Completed"
