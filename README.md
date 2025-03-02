# Wordle Bot

Wordle Bot is a Python-based application that helps you find the best next guess for the Wordle game. It uses entropy calculations to determine the most informative guess based on the feedback from previous guesses.

## Features

- Calculate the best next guess based on entropy
- Web interface to interact with the bot
- Display previous guesses with feedback in a colored box similar to Wordle

## Requirements

- Python 3.x
- Flask
- Progressbar2

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/aayn-a/WordleBotApp.git
   cd WordleBotApp


2. Install the required packages
   pip install flask progressbar2

3. Ensure this directory structure
  WordleBotApp/
  ├── app.py
  ├── wordEliminator.py
  ├── entropyCalculations.py
  ├── validWordleAnswers.txt
  ├── wordlewords.txt
  ├── templates/
  │   └── index.html
  └── static/
      └── styles.css


## Usage
Running the Web Application
Start the Flask application:

Open your web browser and navigate to http://127.0.0.1:5001.

Enter your guess and feedback in the web interface. The bot will display the best next guess and show your previous guesses with feedback.

## Running the Test Script
Run the test script:

The script will print the best next guesses based on the provided guesses and feedback.

## File Descriptions
app.py: The main Flask application that serves the web interface and processes guesses.
wordEliminator.py: Contains the wordEliminator function that filters words based on feedback.
entropyCalculations.py: Contains the calculations function that calculates the entropy for each word.
validWordleAnswers.txt: A text file containing the valid Wordle answers. (https://gist.github.com/cfreshman/a03ef2cba789d8cf00c08f767e0fad7b)
wordlewords.txt: A text file containing the words that can be guessed in Wordle. (https://gist.github.com/dracos/dd0668f281e685bad51479e5acaadb93)
index.html: The HTML template for the web interface.
styles.css: The CSS file for styling the web interface.
test.py: A test script to run the Wordle Bot logic without the web interface.

## Acknowledgements

Flask - A lightweight WSGI web application framework in Python.
Progressbar2 - A text progress bar library for Python.
