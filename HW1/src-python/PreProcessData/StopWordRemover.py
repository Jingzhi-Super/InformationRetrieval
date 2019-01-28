import Classes.Path as Path

# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.
class StopWordRemover:

    def __init__(self):
        # Load and store the stop words from the fileinputstream with appropriate data structure.
        # NT: address of stopword.txt is Path.StopwordDir.
        self.stopwords = set()
        with open(Path.StopwordDir, 'r') as line:
            word = line.readline()
            while word:
                self.stopwords.add(word.rstrip('\n'))
                word = line.readline()
        return

    def isStopword(self, word):
        # Return true if the input word is a stopword, or false if not.
        if word in self.stopwords:
            return True
        return False
