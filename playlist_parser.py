import csv
 
with open("/Users/ethandjay/Downloads/kwur22-d31-2017-12-06-YZpQIe0F.csv", "r") as file:
 
	# Set up CSV reader and process the header
	csv = csv.reader(file)
	header = csv.next()
	artist_ind = header.index("Artist")
	song_ind = header.index("Song")
	 
	# Make an empty list
	song_list = []
	artist_counts = {}
	 
	# Loop through the lines in the file and get each coordinate
	for row in csv:
	    artist = row[artist_ind]
	    song = row[song_ind]
	    song_list.append([artist,song])

	    if artist in artist_counts:
	    	artist_counts[artist] += 1
	    else:	
	    	artist_counts[artist] = 1

	sorted_count = sorted(artist_counts.items(), key=lambda x:x[1])

	for entry in sorted_count:
		print(str(entry[0]) + ": " + str(entry[1]))