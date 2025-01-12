# content of test.py
import unittest
from simple import inc
# Using unittest
class TestSimple(unittest.TestCase):
    def test_inc(self):
        self.assertEqual(inc(3), 4)  # Adjusted to match the function logic
        self.assertEqual(inc(0), 1)
        self.assertEqual(inc(-1), 0)

if __name__ == "__main__":
    unittest.main()

# Using pytest
def test_inc():
    assert inc(3) == 4  # Adjusted to match the function logic
    assert inc(0) == 1
    assert inc(-1) == 0
