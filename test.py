 # %%
from wordEliminator import wordEliminator
from entropyCalculations import read_words_from_file, calculations

wordAnswers = read_words_from_file("validWordleAnswers.txt") #words that can actually be the answer
startingWords = read_words_from_file("wordlewords.txt") #able to be put into wordle

possibleAnswers, possibleStarting = wordEliminator("salet", ["green", "yellow", "yellow", "yellow", "yellow"], wordAnswers, startingWords)
print(possibleAnswers)
print(possibleStarting)
newMap = calculations(possibleAnswers, possibleStarting)
sorted_map = dict(sorted(newMap.items(), key=lambda item: item[1], reverse=True))
tupleList = list(sorted_map.items())

# %%
# %%
