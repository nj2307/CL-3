from mrjob.job import MRJob
import re

class MRWordCount(MRJob):

    def mapper(self, _, line):
        words = re.findall(r'\b\w+\b', line)
        for word in words:
            yield (word.lower(), 1)

    def reducer(self, word, counts):
        yield (word, sum(counts))

if __name__ == '__main__':
    MRWordCount.run()
