class Word:

    def __init__(self):
        self.word = '' # the word the user set
        self.guess = '' # the word the player has to guess
        self.counter = 0 # counts how many times the player has guessed
        self.attemptsLeft = 0 # how many attempts are left
    
    def setWord(self, input):
        self.word = input
    
    def getWord(self):
        return self.word
    
    def setGuess(self, input):
        self.guess = input
    
    def getGuess(self):
        return self.guess
    
    def setAttemptsLeft(self, input):
        self.attemptsLeft = input

    def getAttemptsLeft(self):
        return self.attemptsLeft
    
    def test(self):
        if not len(self.word) == len(self.guess):
            return f'Your guess is {len(self.guess)} letters long, it should be {len(self.word)} letters long.'
        elif self.word == self.guess:
            return f'You guessed the word!'
        else:
            pass