import unittest
import wordswitch

class testwordswitch(unittest.TestCase):
    def test_word_switch(self):
        result = wordswitch.wordswitch(8)
        self.assertEqual(result,"Eight")
        result = wordswitch.wordswitch(1)
        self.assertEqual(result,"One")
        result = wordswitch.wordswitch(4)
        self.assertEqual(result,"Four")


if __name__ == '__main__':
    unittest.main()
