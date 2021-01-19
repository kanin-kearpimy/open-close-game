class OpenCloseGame:
    def __init__(self, player1, bot):
        self.historyTurn = []
        self.player = player1
        self.bot = bot
        self.isPlayerPredictor = True

    def startGame(self):
        print('\n You are {}. '.format('Predictor' if self.isPlayerPredictor else 'Player'))
        playerAnswerInput = input()

        play_1_ans = self.player.playAnswer(self.isPlayerPredictor, playerAnswerInput)
        bot_ans = self.bot.playAnswer(not self.isPlayerPredictor)

        if(play_1_ans['status'] != True):
            print(play_1_ans['message'])
            return False

        if(bot_ans['status'] != True):
            print(bot['message'])
            return False

        gameResult = self.checkWinner(self.player.checkAnswer()['playerAnswer'], self.bot.checkAnswer()['playerAnswer'])

        print("Player Answer is: " + self.player.checkAnswer()['playerAnswer'])
        print("Bot Answer is: " + self.bot.checkAnswer()['playerAnswer'])

        if(gameResult['gotWinner']):
            print('=====\n')
            print(gameResult['message'])
            print('=====\n')
            return True

        self.isPlayerPredictor = not self.isPlayerPredictor

        return False

    def checkWinner(self, answer1, answer2):
        allAnswer = (answer1 + answer2).lower()
        allAnswerSorted = self.sortStringFollowedByNumber(allAnswer)
        prediction = allAnswerSorted[-1]
        result = {}

        if(int(allAnswerSorted.count('o')) == int(prediction)):
            if(self.isPlayerPredictor):
                result = {
                    'message': 'The Winner is PLAYER'
                }
            else:
                result = {
                    'message': 'The Winner is BOT'
                }
            result['gotWinner'] = True
        else:
            result = {
                'gotWinner': False
            }

        return result

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
