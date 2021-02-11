import unittest
from Library.Single_Character_Parcer import Single_Character_Parcer
from Library.Actions import Actions

class TestSingle_Character_Parcer(unittest.TestCase):
    def test_parce_info(self):
        s = Single_Character_Parcer(Actions)
        action, amount = s.parce_info("L")
        self.assertTrue(action == Actions.Show)
        self.assertTrue(amount == 0)
        action, amount = s.parce_info("lakan")
        self.assertTrue(action == Actions.Skip)
        self.assertTrue(amount == 0)
        action, amount = s.parce_info("q")
        self.assertTrue(action == Actions.Quit)
        self.assertTrue(amount == 0)
        action, amount = s.parce_info("quorn")
        self.assertTrue(action == Actions.Skip)
        self.assertTrue(amount == 0)
        action, amount = s.parce_info("s2")
        self.assertTrue(action == Actions.Sell)
        self.assertTrue(amount == 2)
        action, amount = s.parce_info("i3")
        self.assertTrue(action == Actions.Delivery)
        self.assertTrue(amount == 3)
        action, amount = s.parce_info("i34f")
        self.assertTrue(action == Actions.Skip)
        self.assertTrue(amount == 0)

if __name__ == '__main__':
    unittest.main()

        #self.assertEqual(s.parce_info("s2"), (Actions.Sell, 2))
