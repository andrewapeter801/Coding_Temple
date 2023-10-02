import unittest

from whiteboard import solution

class MatchTestCase(unittest.TestCase):
    def test_example_one(self):
        self.assertEqual(solution([ 'T_T', ':D', ':|', ':)', ':(' ], False),[ 'T_T', ':(', ':|', ':)', ':D' ])
    def test_example_two(self):
        self.assertEqual(solution([':D', ':|', ':)', ':(', ':D' ],True),[':D', ':D', ':)', ':|', ':('])
    def test_example_three(self):
        self.assertEqual(solution([':D', ':|', ':)', ':(', ':D' ],False),[':(', ':|', ':)', ':D', ':D'])
    def test_empty(self):
        self.assertEqual(solution([],True),[])

if __name__ == '__main__':
    unittest.main()