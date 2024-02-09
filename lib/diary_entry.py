import math

class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string


    def __init__(self, title, contents): # title, contents are strings
        # Side-effects:
        #   Sets the title and contents properties
        self.contents = contents
        self.title = title

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