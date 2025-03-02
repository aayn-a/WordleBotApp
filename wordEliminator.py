def wordEliminator(wordGuessed, info, wordList, startingWords):
    def filter_words(words, wordGuessed, info):
        remainingWords = words.copy()  # Create a copy of the word list to iterate over
        for index, color in enumerate(info):
            newRemainingWords = []  # Create a new list to store the remaining words
            for currentWord in remainingWords:
                letter = wordGuessed[index]
                if color == "yellow":
                    # Letter must be in the word but not in the same position
                    if letter in currentWord and currentWord[index] != letter:
                        newRemainingWords.append(currentWord)
                elif color == "green":
                    # Letter must be in the same position
                    if currentWord[index] == letter:
                        newRemainingWords.append(currentWord)
                else:  # color == "gray"
                    # Letter must not be in the word at all, or it must be in the word but already accounted for by green/yellow
                    if letter not in currentWord or (letter in currentWord and wordGuessed.count(letter) > currentWord.count(letter)):
                        newRemainingWords.append(currentWord)
            remainingWords = newRemainingWords  # Update the remaining words list
        return remainingWords

    remainingWords = filter_words(wordList, wordGuessed, info)
    remainingWords2 = filter_words(startingWords, wordGuessed, info)
    
    return remainingWords, remainingWords2