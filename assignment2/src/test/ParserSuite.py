import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_short_vardecl(self):
        """Test short variable declaration"""
        input = """delta: integer = 3;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 101))


