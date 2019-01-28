import sys
sys.path.insert(0, '../')

import Classes.Path as Path
import re

# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.
class TrectextCollection:

    def __init__(self):
        # 1. Open the file in Path.DataTextDir.
        # 2. Make preparation for function nextDocument().
        # NT: you cannot load the whole corpus into memory!!
        self.reader = open(Path.DataTextDir, 'r')
        return

    def nextDocument(self):
        # 1. When called, this API processes one document from corpus, and returns its doc number and content.
        # 2. When no document left, return null, and close the file.
        docNo = ""
        content = ""
        line = self.reader.readline()
        while line != "<DOC>\n":
            line = self.reader.readline()
            if line == "":
                return
        while line[:7] != "<DOCNO>":
            line = self.reader.readline()
        line = re.sub("<.*?>", '', line)
        docNo += line
        while line != "<TEXT>\n":
            line = self.reader.readline()
        line = self.reader.readline()
        while line != "</TEXT>\n":
            content += line
            line = self.reader.readline()
        return [docNo, content]
