import random
import re
import os

class MarkovChain(object):
    """text generation using 2nd order word-level markov chain
    """

    def __init__(self):
        self.chain = {}
        self.w1 = '\n'
        self.w2 = '\n'


    def load_file(self, filename, times=1):
        """to balance out texts of different length, it is often useful to load
        a file into the chain multiple times
        """
        for i in xrange(times):
            self._process_file(filename)

    def generate_text(self, min_words=30):
        min_words = int(min_words)
        self._get_words()
        text = self._pick_word()
        # make sure we start with a capital letter
        # this block is kind of awkward, think about it
        while not text[0].isupper():
            text = self._pick_word()
            self._get_words()
        self._get_words()

        i = 1
        can_continue = True

        while can_continue:
            new_word = self._pick_word()
            text = text + ' ' + new_word
            if i >= min_words and new_word[-1] in ['.', '!', '?']:
                can_continue = False
            else:
                self.words = (self.words[1], new_word)
            i += 1
        return text


    def _get_words(self):
        self.words = random.choice(self.chain.keys())
        # self.word1 = self.words[0]
        # self.word2 = words[1]

    def _pick_word(self):
        return random.choice(self.chain[self.words])

    def _process_file(self, filename):
        fp = open(os.path.dirname(__file__) + '/texts/' + filename)
        for line in fp:
            line = self._clean_line(line)
            if not line.isupper():
                for cword in line.split():
                    if cword != "":
                        cword = self._clean_word(cword)
                        self.chain.setdefault((self.w1, self.w2),
                                              []).append(cword)
                        self.w1 = self.w2
                        self.w2 = cword

    def _clean_line(self, line):
        """make line be gooder
        """
        m = re.match('^[^a-zA-Z]*(.*)', line)
        line = m.group(1)
        line.replace('"', '')
        return line

    def _clean_word(self, word):
        """make word more good
        """
        if word[0] == "'":
            word = word[1:]
        if word[-1] == "'":
            word = word[:-1]
        return word


