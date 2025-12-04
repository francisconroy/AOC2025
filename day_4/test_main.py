from unittest import TestCase

from main import count_adjacents_in_subgrid


class Test(TestCase):
    def test_count_adjacents_in_subgrid(self):
        self.assertEqual(2, count_adjacents_in_subgrid([["1", "2", "@"],
                                                        ["4", "5", "6"],
                                                        ["7", "@", "9"]]))

        self.assertEqual(4, count_adjacents_in_subgrid([["", "", ""],
                                                        ["@", "@", "@"],
                                                        ["@", "", "@"]]))
