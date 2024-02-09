from lib.music_library import *

def test_initially_no_music_library():
    library = MusicLibrary()
    assert library.all() == []
# ...