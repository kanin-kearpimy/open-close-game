import re as Regex
import random

class Player:
    def __init__(self, player, isBot=False):
        self.player = player
        self.isBot = isBot

    def playAnswer(self, isPredictor, answer=''):
        if(self.isBot == True):
            answer = self.generateBotAnswer()
            if(isPredictor):
                answer += str(random.randint(1, 4))

        validate = self.validate(answer, isPredictor)
        if(validate['status'] == False):
            return validate
        
        self.answer = answer

        return validate

    def checkAnswer(self):
        return { 'playerName': self.player, 'playerAnswer': self.answer }
    
    def generateBotAnswer(self):
        ansString = ''
        for i in range(0, 2):
            ansString += random.choice('co')
        return ansString

    def validate(self, answer, predictor):
        predictorRegex = "^[COco][COco][0-4]"
        noPredictorRegex = "^[COco][COco]"

        isPass = {"status": True, "message": "Everything is alright."}
        if(predictor):
            if(Regex.search('[0-9]', answer[-1]) != None and int(answer[-1]) > 4 and len(answer) == 3):
                isPass = {"status": False, "message": "Bad input: prediction should be in the range of 0-4. \nNoticed: Predictor input example: 'CO2' or 'co2'"}
            elif((len(answer) != 3) or Regex.search(predictorRegex, answer) == None):
                isPass = {"status": False, "message": "Bad input: correct input should be of the form CC3, where the first two letters indicate [O]pen or [C]losed state for each hand, followed by the prediction (0-4). \nNoticed: Predictor input example: 'CO2' or 'co2'"}

        else:
            if((len(answer) != 2) or Regex.search(noPredictorRegex, answer) == None):
                isPass = {"status": False, "message": "Bad input: correct input should be of the form CC3, where the first two letters indicate [O]pen or [C]losed state for each hand, followed by the prediction (0-4). \nNoticed: Player input example: 'oo' or 'oo'"}
                if(len(answer) == 2 and answer[-1].isnumeric()):
                    isPass = {"status": False, "message": "Bad input: no prediction expected, you are not the predictor. \nNoticed: Player input example: 'oo' or 'oo'"}

        return isPass
