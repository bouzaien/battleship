import unittest

from src.Battleship import *


class ClassTest(unittest.TestCase):

    def test_battleship(self):
        """
        Test if all ship cells are in the field
        """
        bs = Battleship()
        for ship in bs.ships:
            for cell in ship.cells:
                self.assertIn(cell.coords, bs.field.cells), "Should be True"

    def test_superposed_ships(self):
        """
        Test if there are superposed ships in the field
        """
        bs = Battleship()
        self.assertEqual(set(bs.ships[0].cells).intersection(set(bs.ships[1].cells)), set({})), "Should be True"

    def test_ship_size(self):
        ship = Ship((1,5))
        self.assertEqual(ship.size, (1,5)), "Should be (1,5)"


if __name__ == '__main__':
    unittest.main()
