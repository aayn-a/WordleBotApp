from flask import Flask, render_template, request, jsonify
from wordEliminator import wordEliminator
from entropyCalculations import read_words_from_file, calculations

app = Flask(__name__, template_folder='templates')

wordAnswers = read_words_from_file("validWordleAnswers.txt")
startingWords = read_words_from_file("wordlewords.txt")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_guess', methods=['POST'])
def process_guess():
    guess = request.form['guess']
    feedback = request.form['feedback'].split(',')
    global wordAnswers, startingWords
    wordAnswers, startingWords = wordEliminator(guess, feedback, wordAnswers, startingWords)
    newMap = calculations(wordAnswers, startingWords)
    sorted_map = dict(sorted(newMap.items(), key=lambda item: item[1], reverse=True))
    tupleList = list(sorted_map.items())
    best_guess = tupleList[0][0]
    print(tupleList)

    return jsonify(best_guess=best_guess)

if __name__ == '__main__':
    app.run(port=5001, debug=True)