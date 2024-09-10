import unittest
from unittest import mock
from io import StringIO
from collections import defaultdict

from main import parse_match, update_scores, rank_teams, print_rankings, main


class TestLeagueRanking(unittest.TestCase):

    def test_parse_match(self):
        self.assertEqual(parse_match("Lions 3, Snakes 1"), ("Lions", 3, "Snakes", 1))
        self.assertEqual(parse_match("Tarantulas 0, FC Awesome 0"), ("Tarantulas", 0, "FC Awesome", 0))

    def test_update_scores(self):
        teams = defaultdict(int)
        # Lions win
        update_scores(teams, "Lions", 3, "Snakes", 1)
        self.assertEqual(teams["Lions"], 3)
        self.assertEqual(teams["Snakes"], 0)

        # Draw
        update_scores(teams, "Lions", 1, "Snakes", 1)
        self.assertEqual(teams["Lions"], 4)  # 3 + 1
        self.assertEqual(teams["Snakes"], 1)  # 0 + 1

        # Snakes win
        update_scores(teams, "Snakes", 2, "FC Awesome", 0)
        self.assertEqual(teams["Snakes"], 4)  # 1 + 3
        self.assertEqual(teams["FC Awesome"], 0)

    def test_rank_teams(self):
        teams = {"Lions": 5, "Snakes": 1, "Tarantulas": 6, "FC Awesome": 1, "Grouches": 0}
        expected_rankings = [
            ("Tarantulas", 6),
            ("Lions", 5),
            ("FC Awesome", 1),
            ("Snakes", 1),
            ("Grouches", 0)
        ]
        self.assertEqual(rank_teams(teams), expected_rankings)

    def test_print_rankings(self):
        rankings = [("Tarantulas", 6), ("Lions", 5), ("FC Awesome", 1), ("Snakes", 1), ("Grouches", 0)]
        expected_output = """\
1. Tarantulas, 6 pts
2. Lions, 5 pts
3. FC Awesome, 1 pt
3. Snakes, 1 pt
5. Grouches, 0 pts
"""
        with StringIO() as buf, unittest.mock.patch('sys.stdout', new=buf):
            print_rankings(rankings)
            self.assertEqual(buf.getvalue(), expected_output)

    def test_integration(self):
        input_data = """Lions 3, Snakes 3
Tarantulas 1, FC Awesome 0
Lions 1, FC Awesome 1
Tarantulas 3, Snakes 1
Lions 4, Grouches 0"""
        expected_output = """1. Tarantulas, 6 pts
2. Lions, 5 pts
3. FC Awesome, 1 pt
3. Snakes, 1 pt
5. Grouches, 0 pts
"""

        input_buf = StringIO(input_data)
        output_buf = StringIO()

        with mock.patch('sys.stdin', new=input_buf), mock.patch('sys.stdout', new=output_buf):
            main()

        self.assertEqual(output_buf.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
