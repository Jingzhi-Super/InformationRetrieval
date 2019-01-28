import Classes.Path as Path
from nltk.stem import PorterStemmer


# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.
class WordNormalizer:

    def __init__(self):
        self.ps = PorterStemmer()
        return

    def lowercase(self, word):
        # Transform the word uppercase characters into lowercase.
        # useless as PorterStemmer already does this
        return word.lower()

    def stem(self, word):
        # Return the stemmed word with Stemmer in Classes package.
        word = self.ps.stem(word)
        return word
