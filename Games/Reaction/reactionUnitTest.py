import unittest
from reactiontest import calculate_reaction_time

class TestReaction(unittest.TestCase):

    def test_calculate_reaction_time(self):
        start_time = 0
        end_time = 1000
        expected_result = 1000
        result = calculate_reaction_time(start_time, end_time)
        self.assertEqual(result, expected_result)

        start_time = 500
        end_time = 1500
        expected_result = 1000
        result = calculate_reaction_time(start_time, end_time)
        self.assertEqual(result, expected_result)

        start_time = 1000
        end_time = 2000
        expected_result = 1000
        result = calculate_reaction_time(start_time, end_time)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()