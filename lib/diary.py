import math

class Diary:
    def __init__(self):
        self._diary_list = []

    def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        self._diary_list.append(entry)
        

    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        return self._diary_list

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        # iterate across the list of the diary entries and then add the word count.
        total_word_count = 0
        for diary_entry in self._diary_list:
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
    
        for diary_entry in self._diary_list:
            if diary_entry.count_words() >= highest_word_count and diary_entry.count_words()  < word_capacity:
                highest_word_count = diary_entry.count_words()
                satisfies_word_capacity_diary_entry = diary_entry
        
        return satisfies_word_capacity_diary_entry

        


