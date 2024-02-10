from lib.diary import *
import pytest

'''
Diary: Given no entries, create an instance of a diary 

'''
def test_diary_instance_empty_no_entries():
    diary = Diary()
    assert diary._diary_entries == []

'''
Diary: Given no entries, count of the instances of diary is zero

'''
def test_diary_instance_empty_no_entries_word_count_zero():
    diary = Diary()
    assert diary.count_words() == 0


'''
Diary: Initially, reading time should raise an error as there are no entries! 

'''
def test_diary_instance_empty_no_entries_reading_time_raises_exception():
    diary = Diary()
    with pytest.raises(Exception) as err:
        diary.reading_time(2)
    
    assert str(err.value) == "No entries added yet"


'''
Diary: Initially, find best entry for reading time should raise an error as there are no entries! 

'''
def test_diary_instance_empty_no_entries_best_entry_reading_time_raises_exception():
    diary = Diary()
    with pytest.raises(Exception) as err:
        diary.find_best_entry_for_reading_time(2,2)
    
    assert str(err.value) == "No entries added yet"




'''
Could also do additional tests for the incorrect wpm values e.g if wpm is not an integer or is < 0

'''