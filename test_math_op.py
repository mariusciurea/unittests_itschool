import unittest
import math_operations as mo


class TestMath(unittest.TestCase):
    def test_inmultire(self):
        self.assertEqual(mo.inmultire(10, 7), 70)
        self.assertEqual(mo.inmultire(-1, 100), -100)
        self.assertEqual(mo.inmultire(0, 234523534563456), 0)
        self.assertEqual(mo.inmultire(29384234, 312343421), 29384234 * 312343421)

    def test_impartire(self):
        self.assertEqual(mo.impartire(10, 2), 5.0)
        self.assertEqual(mo.impartire(5, 2), 2.5)
        self.assertEqual(mo.impartire(0, 234523534563456), 0)
        # self.assertEqual(mo.impartire(7, 0), None)
        self.assertRaises(ValueError, mo.impartire, 7, 0)


        # self.assertRaises(ValueError, mo.impartire, 5, 0)


if __name__ == '__main__':
    unittest.main()
