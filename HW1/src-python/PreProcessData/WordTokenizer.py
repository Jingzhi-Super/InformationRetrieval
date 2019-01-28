# import Classes.Path as Path
from collections import deque


# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.
class WordTokenizer:

    def __init__(self, content):
        # Tokenize the input texts.
        table = str.maketrans(dict.fromkeys('''0123456789(),.;:&#*!/|@?$%=^+-[]{\\}~'"'''))
        self.tokenizer = deque(content.translate(table).split())
        return

    def nextWord(self):
        # Return the next word in the document.
        # Return null, if it is the end of the document.
        word = None
        if self.tokenizer:
            word = self.tokenizer.popleft()
        return word

