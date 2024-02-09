from lib.diary import *
from lib.diary_entry import *

# Test-drive a class system based on this design.

'''
Context to the multiclass: 

Class (1)I have a diary: 

where I want to count the words etc. of the diary entries

1) I create a diary
2) I can add a diary entry to the diary
3) I can see list of diary entries  
4) I can count all the words of all diary entries
5) Calulate the total reading time of the diary entries within the diary
6) I can pull out the diary entry most appropriate to the reading time available
has to be < = to the words that can be read in that timeframe

Class (2)  The diary entry : 

With in the diary entry , want to be able to:

1) Create a diary entry with a title and content inputted 
2) count the content words within each diary entry
3) caluclate the reading time of the diary entry
4) given certain number of minutes, give me a chunk of the diary entry 
i can read in that time

'''



'''
Integrated: Given a diary entry , add it to the empty diary
'''

def test_diary_entries_added_to_empty_diary():
    diary = Diary()
    diary_entry_1 = DiaryEntry("First day at Makers", "This was an intense start to the week.")
    diary.add(diary_entry_1)
    assert diary.all() == [diary_entry_1]

'''
Integrated: Given diary entry added to the existing list, 
add it to the list of diary entries

'''

def test_diary_entries_added_to_non_empty_diary():
    diary = Diary()
    diary_entry_1 = DiaryEntry("First day at Makers", "This was an intense start to the week.")
    diary_entry_2 = DiaryEntry("Second day at Makers", "This is the second entry to the diary.")
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    assert diary.all() == [diary_entry_1, diary_entry_2]


'''
Integrated: Given diary entry added to the existing list, 
add it to the list of diary entries and calculate the total number of words.

'''

def test_diary_entries_added_to_non_empty_diary_counting_total_words():
    diary = Diary()
    diary_entry_1 = DiaryEntry("Skipping through life", "This was an intense start to the week.")
    diary_entry_2 = DiaryEntry("2nd January 2024", "This is the second entry to the diary.")
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    assert diary.count_words() == 16


'''
Integrated: Given diary entry added to the existing list, 
add it to the list of diary entries and calculate the total reading time of the entries.

'''

def test_diary_entries_added_to_non_empty_diary_calculate_total_read_time():
    diary = Diary()
    diary_entry_1 = DiaryEntry("1st Jan 2024", "Got a run in and what a feeling!")
    diary_entry_2 = DiaryEntry("2nd January 2024", "Keeping up the momentum as I skip through 2024.")
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    assert diary.reading_time(200) == 1



'''
Integrated: Given a long diary entry added to the existing list, 
add it to the list of diary entries and calculate the total reading time of the entries.

'''

def test_diary_entries_added_to_non_empty_diary_calculate_total_read_time():
    diary = Diary()
    diary_entry_1 = DiaryEntry("1st Jan 2024", "Got a run in and what a feeling!")
    diary_entry_2 = DiaryEntry("2nd January 2024", " ".join("word" for i in range(400)))
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    assert diary.count_words() == 408
    assert diary.reading_time(200) == 3


'''
Integrated: Given two long diary entries find best entry given the number of available minutes to read ,
both entries are under the total words they can read => choose the one closest to that number

'''

def test_diary_entries_added_to_non_empty_diary_entries_less_than_words():
    diary = Diary()
    diary_entry_1 = DiaryEntry("1st Jan 2024", " ".join("word" for i in range(300)))
    diary_entry_2 = DiaryEntry("2nd January 2024", " ".join("word" for i in range(390)))
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    assert diary.count_words() == 700
    assert diary.reading_time(200) == 4
    assert diary.find_best_entry_for_reading_time(200,2) == diary_entry_2



'''
Integrated: Given two long diary entries find best entry given the number of available minutes to read 
one entry is over, and one entry is under => choose the one closest to and less than that number

'''

def test_diary_entries_added_to_non_empty_diary_mix_entries():
    diary = Diary()
    diary_entry_1 = DiaryEntry("1st Jan 2024", " ".join("word" for i in range(425)))
    diary_entry_2 = DiaryEntry("2nd January 2024", " ".join("word" for i in range(800)))
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    assert diary.count_words() == 1225
    assert diary.reading_time(230) == 6
    assert diary.find_best_entry_for_reading_time(230,2) == diary_entry_1


'''
Integrated: Given two long diary entries find best entry given the number of available minutes to read ,
one entry under the total words and one equal to the total words they can read => choose the equal number of words

'''

def test_diary_entries_added_to_non_empty_diary_entries_equal_to_words():
    diary = Diary()
    diary_entry_1 = DiaryEntry("1st Jan 2024", " ".join("word" for i in range(300)))
    diary_entry_2 = DiaryEntry("2nd January 2024", " ".join("word" for i in range(400)))
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    assert diary.count_words() == 700
    assert diary.reading_time(200) == 4
    assert diary.find_best_entry_for_reading_time(200,2) == diary_entry_2


'''
Integrated: Given multiple long diary entries find 1st entry given the number of available minutes to read ,
one entry under the total words and one equal to the total words they can read => choose the equal number of words
# assuming later date will be chosen if two entries have the same word count
'''

def test_diary_entries_added_to_non_empty_diary_entries_equal_to_words():
    diary = Diary()
    diary_entry_1 = DiaryEntry("1st Jan 2024", " ".join("word" for i in range(300)))
    diary_entry_2 = DiaryEntry("2nd January 2024", " ".join("word" for i in range(400)))
    diary_entry_3 = DiaryEntry("3rd January 2024", " ".join("word" for i in range(400)))
    diary.add(diary_entry_1) 
    diary.add(diary_entry_2)
    diary.add(diary_entry_3)
    assert diary.count_words() == 1100
    assert diary.reading_time(200) == 6
    assert diary.find_best_entry_for_reading_time(200,2) == diary_entry_2