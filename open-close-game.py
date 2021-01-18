import re as Regex
import random

class Player:
    def __init__(self, player, isBot=False):
        self.player = player
        self.isBot = isBot

    def playAnswer(self, answer, isPredictor):
        validate = self.validate(answer, isPredictor)
        if(validate['status'] == False):
            return validate
        self.answer = answer
        return validate

    def botAnswer(self, isPredictor):
        if(self.isBot != True):
            print("You Are not bot !!!")
            return False
        ansString = self.generateBotAnswer()
        if(isPredictor):
            ansString += str(random.randint(1, 4))

        self.answer = ansString

    def checkAnswer(self):
        return { 'playerName': self.player, 'playerAnswer': self.answer }

    def isBot(self):
        return self.isBot
    
    def generateBotAnswer(self):
        ansString = ''
        for i in range(0, 2):
            ansString += random.choice('co')
        return ansString

    def validate(self, answer, predictor):
        predictorRegex = "^[COco][COco][1-4]"
        noPredictorRegex = "^[COco][COco]"

        isPass = {"status": True, "message": "Everything is alright."}
        if(predictor):
            if( (len(answer) != 3) or Regex.search(predictorRegex, answer) == None):
                isPass = {"status": False, "message": "You are predictor, please type as format: 'CO2'."}
        else:
            if((len(answer) != 2) or Regex.search(noPredictorRegex, answer) == None):
                isPass = {"status": False, "message": "You are user, please type as format: 'CC'."}

        return isPass

class OpenCloseGame:
    def __init__(self):
        self.setPlayerPredictor = True
        self.historyTurn = []

    def checkWinner(self, answer1, answer2):
        allAnswer = (answer1 + answer2).lower()
        allAnswerSorted = self.sortStringFollowedByNumber(allAnswer)
        prediction = allAnswerSorted[-1]
        result = {}

        if(int(allAnswerSorted.count('o')) == int(prediction)):
            if(self.setPlayerPredictor):
                result = {
                    'gotWinner': True,
                    'playerWin': self.setPlayerPredictor,
                    'message': 'The Winner is PLAYER'
                }
            else:
                result = {
                    'gotWinner': True,
                    'playerWin': self.setPlayerPredictor,
                    'message': 'The Winner is BOT'
                }
        else:
            result = {
                'gotWinner': False
            }
            self.setPlayerPred()

        return result

    def setPlayerPred(self):
        self.setPlayerPredictor = not self.setPlayerPredictor


    def sortStringFollowedByNumber(self, string):
        alphas = []
        digits = []
        result = ''

        for character in string:
            if(character.isalpha()):
                alphas.append(character)
            else:
                digits.append(character)
        
        result = ''.join(alphas+digits)

        return result
    


bot = Player('bot', isBot=True)
player_1 = Player('player_1', isBot=False)
playerPredictor = True
game = OpenCloseGame()

while True:
    playerAnswerInput = input()

    play_1_ans = player_1.playAnswer(playerAnswerInput, playerPredictor)

    if(play_1_ans['status'] != True):
        print(play_1_ans['message'])
        continue

    bot.botAnswer(not playerPredictor)

    print("Player Answer is: " + player_1.checkAnswer()['playerAnswer'])
    print("Bot Answer is: " + bot.checkAnswer()['playerAnswer'])

    gameResult = game.checkWinner(player_1.checkAnswer()['playerAnswer'], bot.checkAnswer()['playerAnswer'])
    
    if(gameResult['gotWinner']):
        print(gameResult['message'])
        break

    playerPredictor = not playerPredictor
