class Sentence(object):

    def __init__(self, sentence):
        if isinstance(sentence, str):
            self.sentence = sentence
        else:
            raise TypeError("Sentence must be a String object")
    
    def list_distinct_upper_lower_cases(self):
        """
        Transform the sentence (String object) in a list of 0 and 1.
        Represent Lowercase by 0.
        Represent Uppercase by 1.
        """
        return [1 if e.isupper() else 0 for e in self.sentence ]

    def count_words(self):
        """
        Number of words equal to:
        - Count of ones in list_distinct_upper_lower_cases(self)
        - (+1) for the first word of the sentence
        """
        return 1 + sum(self.list_distinct_upper_lower_cases())

if __name__ == '__main__':
    sentence_string = "thisIsATestToCountNumberOfWordsInASentenceWithUpperAndLowerCase"
    sentence_object  = Sentence(sentence_string)
    print(sentence_object.count_words())

