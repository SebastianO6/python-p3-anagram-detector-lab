class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, word_list):
        sorted_word = sorted(self.word)
        matches = []

        for candidate in word_list:
            if candidate.lower() != self.word and sorted(candidate.lower()) == sorted_word:
                matches.append(candidate)

        return matches        