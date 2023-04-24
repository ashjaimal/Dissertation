import unittest
from unittest.mock import MagicMock
from memory_game import MemoryGame


class TestMemoryGame(unittest.TestCase):

    def test_start_game(self):
        main_menu_callback = MagicMock()
        memory_game = MemoryGame(main_menu_callback)
        memory_game.start_game()

        self.assertEqual(len(memory_game.sequence), memory_game.level)
        self.assertEqual(memory_game.sequence_label.text(), ' '.join(map(str, memory_game.sequence)))

    def test_hide_sequence(self):
        main_menu_callback = MagicMock()
        memory_game = MemoryGame(main_menu_callback)
        memory_game.start_game()
        memory_game.hide_sequence()

        self.assertEqual(memory_game.sequence_label.text(), 'Numbers hidden. Enter the sequence.')

    def test_check_answer_correct(self):
        main_menu_callback = MagicMock()
        memory_game = MemoryGame(main_menu_callback)
        memory_game.sequence = [1, 2, 3]
        memory_game.user_input.setText("1 2 3")

        memory_game.check_answer()

        self.assertEqual(memory_game.result_label.text(), 'Correct! Well done! Move onto the next level.')

    def test_check_answer_incorrect(self):
        main_menu_callback = MagicMock()
        memory_game = MemoryGame(main_menu_callback)
        memory_game.sequence = [1, 2, 3]
        memory_game.user_input.setText("1 2 4")

        memory_game.check_answer()

        self.assertEqual(memory_game.result_label.text(), 'Incorrect. Game over. Your score: 0')


if __name__ == '__main__':
    unittest.main()