from feedback import getFeedback
import math
import progressbar




bar = progressbar.ProgressBar(max_value=100)
def updateFeedback(feedback, map):
    tupley = tuple(feedback)
    if tupley in map:
        map[tupley] += 1
    else:
        map[tupley] = 1


def read_words_from_file(file_path):
    with open(file_path, 'r') as file:
        words = file.read().split()
    return words


def calculations(wordAnswers, possibleStarting):
    wordEntropys = {}
    counter = 0
    for currentWord in possibleStarting:
        map = {}
        for word in wordAnswers:
            feedback = getFeedback(currentWord, word)
            updateFeedback(feedback, map)
        probabilities = {key: value / len(wordAnswers) for key, value in map.items()}
        bitsInfo = {key: math.log2(1/value) for key, value in probabilities.items()}
        entropy = 0
        bValues = list(bitsInfo.values())
        pValues = list(probabilities.values())
        for i in range(len(bValues)):
            entropy += bValues[i] * pValues[i]
        wordEntropys[currentWord] = entropy
        bar.update(counter)
        counter = counter + (1/(len(possibleStarting)) * 100)
    return wordEntropys

