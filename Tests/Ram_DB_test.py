import unittest
from Library.Ram_DB import Ram_DB

class TestRam_DB(unittest.TestCase):
    def test_add(self):
        r=Ram_DB()
        r.add(3)
        self.assertEqual(r.stock, 3)
        r.add(5)
        self.assertEqual(r.stock, 8)
        r.add(-3)
        self.assertEqual(r.stock, 8)
        with self.assertRaises(TypeError):
            r.add(-3)
            #gör så att man inte kan lägga in - på add
            #-m unittest Tests.Ram_DB_test


if __name__ == '__main__':
    unittest.main()