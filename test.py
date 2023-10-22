import unittest
from main import to_upper

class MyTestCase(unittest.TestCase):
    def test(self):
        name="Madhuban"
        up=to_upper(name)
        self.assertEqual(up,"MADHUBAN")

if __name__ == '__main__':
    unittest.main()