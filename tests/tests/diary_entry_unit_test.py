from lib.diary_entry import *

# Given a title and contents we can instanciate the diary entry

def test_diary_entry_instanciated_with_properties():
    diary_entry_1 = DiaryEntry("My Title", "These are the contents")
    assert diary_entry_1.title == "My Title"
    assert diary_entry_1.content == "These are the contents"


#given the title and contents, we can count the words of the in the diary contents
    
def test_contents_count_words_longer_string_content():
    contents = " ".join("word" for i in range(400))
    diary_entry = DiaryEntry("Tuesday 2nd", contents)
    result = diary_entry.count_words()
    assert result == 400


# given a shorter string which results in a reading time of less than a minute, count the words and return 1

def test_given_shorter_string_return_reading_time():
    diary_entry = DiaryEntry("Mon 1st", "Something less than a minute, and isnt very long at all.")
    
    assert diary_entry.count_words() == 11
    assert diary_entry.reading_time(200) == 1

#given a longer string , count the words and reading time 

def test_title_count_words_and_reading_time_given_longer_string_content():
    contents = " ".join("word" for i in range(600))
    diary_entry = DiaryEntry("Wednesday 3rd", contents)

    assert diary_entry.count_words() == 600
    assert diary_entry.reading_time(200) == 3


#given a longer string , count the words and reading time for a float and round up

def test_given_longer_string_content_calculate_float_round_down_reading_time():
    contents = " ".join("word" for i in range(875))
    diary_entry = DiaryEntry("Thursday 4th", contents)

    assert diary_entry.count_words() == 875
    assert diary_entry.reading_time(250) == 4



#given the shorter string and reading time < less than num minutes available it outputs the string itself.
    
def test_given_reading_time_less_than_available_time_return_content():
    contents_sentence_1 = " ".join("word" for i in range(15)) + ". "
    contents_sentence_2 = " ".join("something" for i in range(17)) + ". "
    contents_alternate = contents_sentence_1 + contents_sentence_2
    contents = 5 * contents_alternate
    diary_entry = DiaryEntry("Friday 5th", contents)
    assert diary_entry.reading_time(240) == 1
    assert diary_entry.reading_chunk(240, 6) == contents



#given longer string and reading time > number of minutes available , return a chunk of content suitable for available time
    
def test_given_reading_time_greater_than_available_time():
    contents_sentence_1 = " ".join("word" for i in range(15)) + ". "
    contents_sentence_2 = " ".join("something" for i in range(17)) + ". "
    contents_alternate = contents_sentence_1 + contents_sentence_2
    contents = 100 * contents_alternate
    contents_list = contents.split()
    contents_segment = " ".join(contents_list[0:1440])
    diary_entry = DiaryEntry("Sat 8th", contents)
    assert diary_entry.count_words() == 3200
    assert diary_entry.reading_time(240) == 14
    assert diary_entry.reading_chunk(240, 6) == f"{contents_segment}"


#given longer string and reading time > number of minutes available return the next segment along
    
def test_given_reading_time_greater_than_available_time_next_segment():
    contents_sentence_1 = " ".join("cray" for i in range(18)) + ". "
    contents_sentence_2 = " ".join("bla" for i in range(12)) + ". "
    contents_alternate = contents_sentence_1 + contents_sentence_2
    contents = (20 * contents_alternate) + (10 * contents_alternate) + (30 * contents_alternate)
    contents_list = contents.split()
    contents_segment= " ".join(contents_list[1440:])
    diary_entry = DiaryEntry("Sun 9th", contents)
    diary_entry.reading_chunk(240, 6)
    assert diary_entry.count_words() == 1800
    assert diary_entry.reading_time(240) == 8
    assert diary_entry.reading_chunk(240, 6) == f"{contents_segment}"

#given longer string and reading time > number of minutes available return the next segment along

def test_given_reading_time_greater_than_available_time_next_segment_the_next():
    contents_sentence_1 = " ".join("cray" for i in range(18)) + ". "
    contents_sentence_2 = " ".join("bla" for i in range(12)) + ". "
    contents_alternate = contents_sentence_1 + contents_sentence_2
    contents = (20 * contents_alternate) + (10 * contents_alternate) + (30 * contents_alternate)
    contents_list = contents.split()
    contents_segment= " ".join(contents_list[800:1200])
    diary_entry = DiaryEntry("Sun 9th", contents)
    diary_entry.reading_chunk(200, 2)
    diary_entry.reading_chunk(200, 2)
    assert diary_entry.count_words() == 1800
    assert diary_entry.reading_time(240) == 8
    assert diary_entry.reading_chunk(200, 2) == f"{contents_segment}"

    #given longer string and reading time > number of minutes available return the final segment along

def test_given_reading_time_greater_than_available_time_next_segment_the_next_final():
    contents_sentence_1 = " ".join("cray" for i in range(18)) + ". "
    contents_sentence_2 = " ".join("bla" for i in range(12)) + ". "
    contents_alternate = contents_sentence_1 + contents_sentence_2
    contents = (20 * contents_alternate) + (10 * contents_alternate) + (30 * contents_alternate)
    contents_list = contents.split()
    contents_segment= " ".join(contents_list[1600:1801])
    diary_entry = DiaryEntry("Sun 9th", contents)
    diary_entry.reading_chunk(200, 2)
    diary_entry.reading_chunk(200, 2)
    diary_entry.reading_chunk(200, 2)
    diary_entry.reading_chunk(200, 2)
    assert diary_entry.count_words() == 1800
    assert diary_entry.reading_time(240) == 8
    assert diary_entry.reading_chunk(200, 2) == f"{contents_segment}"