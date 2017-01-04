import spotipy
import urllib
from random import randint
import os
import sys
from pydub import AudioSegment

lz_uri = 'spotify:artist:7oPftvlwr6VrsViSDV7fJY'

spotify = spotipy.Spotify()
# 
resultsForUri = spotify.search(q='year:' + '1960-1969' + ' + ' + 'genre:' + 'rock', type='artist', limit='50')
length = len(resultsForUri['artists']['items'])
if length > 0:
	numItem = randint(0,length-1)
	results = spotify.artist_top_tracks(resultsForUri['artists']['items'][numItem]['uri'])
	artist = resultsForUri['artists']['items'][numItem]['name']
else:
	sys.exit('No Results')


testfile = urllib.URLopener()
numSong = randint(0,9)
print 'Downloaded: ' + results['tracks'][numSong]['name'] + ' - ' + artist
trackName = results['tracks'][numSong]['name']
previewFile = results['tracks'][numSong]['preview_url']
testfile.retrieve(results['tracks'][numSong]['preview_url'], results['tracks'][numSong]['name'])
song = AudioSegment.from_mp3(results['tracks'][numSong]['name'])
os.remove(results['tracks'][numSong]['name'])

duration = 1200

first_3_seconds = song[:duration]
first_3_seconds.export("quizfile.mp3", format="mp3")
