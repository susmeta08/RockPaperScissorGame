import unittest
from Game import Game


class TestClass(unittest.TestCase):

    def test_check_number_of_rounds(self):
        game = Game()
        game.play('rock', 'scissor')
        game.play('paper', 'rock')
        self.assertEqual(game.get_rounds(), 2)

    def test_check_user_score(self):
        game = Game()
        game.play('rock', 'scissor')
        game.play('paper', 'rock')
        game.play('scissor', 'paper')
        self.assertEqual(game. get_user_score(), 3)    


    def test_check_computer_score(self):
        game = Game()
        game.play('rock', 'scissor')
        game.play('paper', 'rock')
        game.play('scissor', 'paper')
        self.assertEqual(game. get_computer_score(), 0)  

    def test_check_winner(self):
        game = Game()
        game.play('rock', 'scissor')
        game.play('paper', 'rock')
        game.play('scissor', 'paper')    
        game.play('paper', 'rock')
        game.play('scissor', 'paper')   
        self.assertEqual(game.get_winner(),'User')      


if __name__ == '__main__':
    unittest.main()        