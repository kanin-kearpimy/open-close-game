from Game import Player, OpenCloseGame

# Game Introduction
print('\n')
print('==========')
print('\n')
print('   Welcome to Open Close Game    ')
print('\n   To play the game, after a count of three, the players will need to simultaneously show their hands with each hand either open or closed, and the predictor need to shout out how many hands they think will be open on total.  ')
print('\n   If the predictor is correct, they win, otherwise the other player becomes the predictor and they go again. This continues until the game is won.   ')
print('\n')
print('==========')

while True:
    # Selection of Choice
    print('Please type number below to choose.')
    print('\n 1 Play Game Now!')
    print('\n 2 Read the rule.')
    print('\n 3 Exit Program.')
    print('\nWould you like to: ')
    userSelect = input()

    if(int(userSelect) == 1):
        bot = Player('bot', isBot=True)
        player_1 = Player('player_1', isBot=False)
        game = OpenCloseGame(player_1, bot)

        while True:
            result = game.startGame()
            if(result):
                break
            else:
                continue

    elif(int(userSelect) == 2):
        print('==========')
        print('\nthe players will need to simultaneously show their hands with each hand either open or closed, and the predictor need to shout out how many hands they think will be open on total.')
        print('\nIf the predictor is correct, they win, otherwise the other player becomes the predictor and they go again. This continues until the game is won.')
        print('\n')
        print('the first two characters will show how you will play your hands, O for open or C for closed.')
        print('\nIf you are the predictor, you also need to enter a third character which is your prediction for how many open hands in total. [0 - 4]')
        print('\nFor example; player 1 as predictor and player 2 as player in this round')
        print('\n player 1: "cc1"')
        print('\n player 2: "co"')
        print('\n Player 1 win because one hand open')
        print('\n')

        while True:
            print('==========')
            print('\n Would you like to exit to menu? ')
            print('\n 1 Yes')
            print('\n 2 No')

            userSelect = input()

            if(int(userSelect) == 1):
                break
            elif(int(userSelect) == 2):
                print('\nYou can choose only 1) Yes\n')
                continue
            else:
                print('\nYou can choose only 1) Yes or 2) No\n')
                continue
    elif(int(userSelect) == 3):
        print('\n Goodbye and See you again soon.')
        break
    else:
        print('\nBad Input: You have only 3 choices\n')
        continue
