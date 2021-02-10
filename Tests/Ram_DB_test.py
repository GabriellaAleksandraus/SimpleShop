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
           r.add("hej")
        self.assertEqual(r.stock, 8)
            #-m unittest Tests.Ram_DB_test

    def test_remove(self):
        r=Ram_DB()
        r.remove(3)
        self.assertEqual(r.stock, 0)
        r.remove(-3)
        self.assertEqual(r.stock, 0)
        r.stock = 5
        r.remove(2)
        self.assertEqual(r.stock, 3)
        r.remove(4)
        self.assertEqual(r.stock, 3)
        r.remove(-2)
        self.assertEqual(r.stock, 3)
        with self.assertRaises(TypeError):
           r.add("hej")
        self.assertEqual(r.stock, 3)

    


if __name__ == '__main__':
    unittest.main()