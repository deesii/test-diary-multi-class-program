from lib.music_library import *

from lib.track import *

"""
When we add two tracks
We get the tracks back in the track list
"""
library = MusicLibrary()
track_1 = Track("Always The Hard Way", "Terror")
track_2 = Track("Higher Place", "Malevolence")
library.add(track_1)
library.add(track_2)
library.tracks # => [track_1, track_2]

"""
When we add two tracks
And we search for a word in the title
We get the matching track back
"""
library = MusicLibrary()
track_1 = Track("Always The Hard Way", "Terror")
track_2 = Track("Higher Place", "Malevolence")
library.add(track_1)
library.add(track_2)
library.search_by_title("Way") # => [track_1]

"""
When we add two tracks
And we search for a small part of a word in the title
We get the matching track back
"""
library = MusicLibrary()
track_1 = Track("Always The Hard Way", "Terror")
track_2 = Track("Higher Place", "Malevolence")
library.add(track_1)
library.add(track_2)
library.search_by_title("lace") # => [track_2]

"""
When we add two tracks
And we search for a word not in any track title
We get an empty list back
"""
library = MusicLibrary()
track_1 = Track("Always The Hard Way", "Terror")
track_2 = Track("Higher Place", "Malevolence")
library.add(track_1)
library.add(track_2)
library.search_by_title("zzz") # => []

"""
Given a track with a title and artist
#format returns a string like TITLE by ARTIST

# this affects just the track, therefore could be in the track test.
"""
track = Track("Higher Place", "Malevolence")
track.format() # => "Higher Place by Malevolence"
