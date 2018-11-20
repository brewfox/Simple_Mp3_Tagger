# Walks current directory and all subdirectories modifying MP3 files found
# Sets ID3 artist tag to directly containing folder
# Sets ID3 song tag to file Name
# Deletes files smaller than 750 KB
# Moves files larger than 10 MB to 'Sets' directory under current directory

import os
import sys
from sets import Set
import subprocess

#Find all MP3 files in current and subdirectory
Files = []
Unique_Bands = Set()
for root, dirs, files in os.walk("."):
	for fil in files:
		if fil.endswith(".mp3"):
			MP3_path = "".join(root) + "".join(dirs) + "/" + fil
			MP3_path = os.path.join(root, fil)
			MP3_full_path = os.path.abspath(MP3_path)
			# Containing folder has Artist Name
			MP3_artist = MP3_full_path.split(os.sep)[-2]
			MP3_song = MP3_full_path.split(os.sep)[-1]

			if MP3_artist == "Sets":
				#Don't re-move/tag things in the Sets folder
				continue

			# Remove files that are too small, and move 'sets'
			MP3_size = os.path.getsize(MP3_path)
			if MP3_size < 750000:
				# Delete files smaller than 750KB
				os.remove(MP3_path)
				print "Removed small file " + str(MP3_size) + ": " + str(MP3_artist) + " " + str(MP3_song)
				continue

			Files.append(MP3_path)
			#new = ['id3v2','--artist', '"'+str(root[2:])+'"', os.path.join(root, fil)]
			#print "file: " + str(fil) + " " + str(new)

			# Call id3v2 to set the Id3 Artist tag to the directory name
			subprocess.check_output(['id3v2','--artist', MP3_artist, MP3_path])
			song_name = os.path.splitext(MP3_song)[0]
			subprocess.check_output(['id3v2','--song', song_name, MP3_path])
 			Unique_Bands.add(MP3_artist)

			if MP3_size > 10000000:
				#Move files bigger than 10MB to 'sets' folder
				set_path = os.path.join(os.path.dirname(MP3_full_path), "Sets")
				print set_path
				if not os.path.isdir(set_path):
					os.mkdir(set_path)
				os.rename(MP3_path, os.path.join(set_path, MP3_song))
				print "Moved set file " + str(MP3_size) + ": " + str(MP3_artist) + " " + str(MP3_song)


print "Found Unique bands: "
print Unique_Bands

print "Script Completed"
