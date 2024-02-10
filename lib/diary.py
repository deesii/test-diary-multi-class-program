import math

class Diary:
    def __init__(self):
        self._diary_entries = []

    def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        self._diary_entries.append(entry)
        

    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        return self._diary_entries

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        # iterate across the list of the diary entries and then add the word count.
        total_word_count = 0
        for diary_entry in self._diary_entries:
            total_word_count += diary_entry.count_words()

        return total_word_count

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        return math.ceil(self.count_words()/ wpm)


    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        word_capacity = wpm * minutes

        highest_word_count = 0
        satisfies_word_capacity_diary_entry = None
    
        for diary_entry in self._diary_entries:
            if diary_entry.count_words() >= highest_word_count and diary_entry.count_words()  <= word_capacity:
                highest_word_count = diary_entry.count_words()
                print (highest_word_count)
                satisfies_word_capacity_diary_entry = diary_entry
                print(satisfies_word_capacity_diary_entry)
        
        return satisfies_word_capacity_diary_entry

        
class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string


    def __init__(self, title, contents): # title, contents are strings
        # Side-effects:
        #   Sets the title and contents properties
        self.contents = contents
        self.title = title
        self.contents_remainder = self.contents.split()

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in the contents
        return len(self.contents.split())

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
        return math.ceil(self.count_words()/ wpm )

    def reading_chunk(self, wpm, minutes):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.
        num_words_can_read =  minutes * wpm #the number of words that a person can read given the time available
        
        if self.count_words() <= num_words_can_read: 
            return self.contents
        else: 
            if len(self.contents_remainder) == self.contents.split() or len(self.contents_remainder) >= num_words_can_read:
                contents_chunk = " ".join(self.contents_remainder[0:num_words_can_read]) 
                self.contents_remainder = self.contents_remainder[num_words_can_read:] 
                return f"{contents_chunk}" 
            else:
                the_last_bit_of_text = " ".join(self.contents_remainder)
                self.contents_remainder = self.contents.split() 
                return the_last_bit_of_text

diary = Diary()
diary_entry_1 = DiaryEntry("1st Jan 2024", " ".join("word" for i in range(300)))
diary_entry_2 = DiaryEntry("2nd January 2024", " ".join("word" for i in range(400)))
diary_entry_3 = DiaryEntry("3rd January 2024", " ".join("word" for i in range(400)))
diary.add(diary_entry_1) 
diary.add(diary_entry_2)
diary.add(diary_entry_3)
print(diary.count_words()) # == 1100
print(diary.reading_time(200)) # == 6
print(diary.find_best_entry_for_reading_time(200,2))  # == diary_entry_3