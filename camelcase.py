sentence = "thisIsATestToCountNumberOfWordsInASentenceWithUpperAndLowerCase"

count_word = sum([1 for e in sentence if e.isupper()]) + 1 
