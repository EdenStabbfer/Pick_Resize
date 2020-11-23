import unittest
from main import pick_resize


class UnitTest(unittest.TestCase):
    def setUp(self):
        self.path = "test_data"
        self.new_path = "new_test_data"
        self.new_size = (32,32)
        
        
    def test_open_anime_pick(self):
        try:
            pick_resize(self.new_size, self.path, self.new_path)
        except AssertionError:
            pass
        

if __name__=="__main__":
    unittest.main()