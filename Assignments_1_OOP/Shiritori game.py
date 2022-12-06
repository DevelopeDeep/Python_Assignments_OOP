class Shiritori:

    def __init__(self):
        self.playedWords = []
        self.currentWord = None
        self.main()

    def ruleOne(self):
        lastWord = self.playedWords[-1]
        if lastWord[-1] == self.currentWord[0]:
            return True
        return False

    def ruleTwo(self):
        if self.currentWord in self.playedWords:
            return False
        return True

    def addWord(self):
        self.playedWords.append(self.currentWord)

    def play(self, word):
        word = word.lower()
        word = word.strip()
        self.currentWord = word
        if not self.playedWords:
            self.addWord()
        elif(self.ruleOne() and self.ruleTwo()):
            self.addWord()
        else:
            self.gameOver()

    def gameOver(self):
        print("You have lost. Game is being restarted.")
        self.playedWords = []
        self.currentWord = None

    def main(self):
        print("Enter a word or enter '' to exit the game")
        while True:
            word = input("Please enter your word>")
            self.play(word)
            if word == '':
                break
        print("Thank you for playing.")

game = Shiritori()
