
from lib.track import *

def test_initially_no_music_library():
    library = MusicLibrary()
    assert library.all() == []
  # ...