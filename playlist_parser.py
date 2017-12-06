import csv
 
with open("/Users/ethandjay/Downloads/kwur22-d31-2017-12-06-YZpQIe0F.csv", "r") as file:

	# Set up CSV reader and process the header
	csv = csv.reader(file)
	header = csv.next()
	artist_ind = header.index("Artist")
	album_ind = header.index("Disk")
	song_ind = header.index("Song")
	 
	# Make an empty list
	song_list = []
	artist_counts = {}
	album_counts = {}
	song_counts = {}
	 
	# Loop through the lines in the file and get each coordinate
	for row in csv:
		artist = row[artist_ind]
		album = row[album_ind]
		song = row[song_ind]
		song_list.append([artist,album,song])

		if artist in artist_counts:
			artist_counts[artist] += 1
		else:	
			artist_counts[artist] = 1

		album_string = artist + " - " + album
		if album_string in album_counts:
			album_counts[album_string] += 1
		else:
			album_counts[album_string] = 1

		song_string = artist + " - " + song
		if song_string in song_counts:
			song_counts[song_string] += 1
		else:
			song_counts[song_string] = 1

	sorted_artist_counts = sorted(artist_counts.items(), key=lambda x:x[1])
	sorted_album_counts = sorted(album_counts.items(), key=lambda x:x[1])
	sorted_song_counts = sorted(song_counts.items(), key=lambda x:x[1])

	print

	print("Top Artists (31 Days):")
	for entry in sorted_artist_counts[-20:]:
		print(str(entry[0]) + ": " + str(entry[1]))

	print

	print("Top Albums (31 Days):")
	for entry in sorted_album_counts[-20:]:
		print(str(entry[0]) + ": " + str(entry[1]))

	print

	print("Top Songs (31 Days):")
	for entry in sorted_song_counts[-20:]:
		print(str(entry[0]) + ": " + str(entry[1]))

	print
