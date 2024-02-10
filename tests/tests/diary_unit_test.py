from lib.diary import *

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