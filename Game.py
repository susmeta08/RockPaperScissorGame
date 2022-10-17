import random
class Game:
    def __init__(self):
        self.user_score = 0
        self.computer_score = 0
        self.total_round = 0

    def is_game_over(self):
        if self.user_score == 5 or self.computer_score == 5:
            return True
        return False

    def play(self, user_option, computer_option):
        self.total_round += 1
        
        if user_option == 'rock':
            if computer_option == 'paper':
                self.computer_score += 1
                return 'Computer Wins'
            elif computer_option == 'scissor':
                self.user_score += 1
                return 'User Wins'    
        elif user_option == 'paper':
            if computer_option == 'scissor':
                self.computer_score += 1
                return 'Computer Wins'
            elif computer_option == 'rock':
                self.user_score += 1
                return 'User Wins'
        elif user_option == 'scissor':
            if computer_option == 'rock':
                self.computer_score += 1
                return 'Computer Wins'
            elif computer_option == 'paper':
                self.user_score += 1  
                return 'User Wins'
        return 'Draw'

    def get_winner(self):
        if self.user_score == 5:
            return 'User'     
        elif self.computer_score == 5:
            return 'Computer'
        return 'No Winner'

    def get_user_score(self):
        return self.user_score   

    def get_computer_score(self):
        return self.computer_score

    def get_rounds(self):
        return self.total_round


def get_computer_choice():
    num = random.randint(0,2)
    if num == 0:
        return 'rock'
    elif num == 1:
        return 'scissor'   
    else:
        return 'paper'      


def get_user_choice():
    while True:
        print('User Choice')
        print('Select from below options')
        print('1. Rock')        
        print('2. Scissor') 
        print('3. Paper')
        print('4. Quit')
        option = int(input('Your choice: '))
        if option == 1:
            return 'rock'
        elif option == 2:
            return 'scissor'
        elif option == 3:
            return 'paper'
        elif option == 4:
            return 'quit'    
        else:
            print('Invalid option')            


def playGame():
    game = Game()   
    while game.is_game_over() is False:
        computer_option = get_computer_choice()
        user_option = get_user_choice()
        if user_option == 'quit':
            return
        print(game.play(user_option, computer_option))
    print('Winner:',game.get_winner())
    print('Total Rounds:',game.get_rounds())


def start():
    while True:
        print('Welcome to the rock paper and scissor game')
        playGame()
        option = int(input('Enter 1 to play again or any other digit to quit: '))
        if option != 1:
            break       


if __name__ == '__main__':
    start()






