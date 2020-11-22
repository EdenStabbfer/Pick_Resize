import unittest
from main import pick_resize


class UnitTest(unittest.TestCase):
    def setUp(self):
        self.anime_path = "data/Anime/"
        self.deer_path = "data/Deers/"
        self.mask_path = "data/Mask/"
        self.new_anime_path = "newData/Anime/"
        self.new_deer_path = "newData/Deers/"
        self.new_mask_path = "newData/Mask/"
        
        self.new_size = (32,32)
        self.errors = 0
        
        
    def test_open_anime_pick(self):
        try:
            pick_resize(self.new_size, self.anime_path, self.new_anime_path)
        except AssertionError:
            pass
    
    def test_open_deer_pick(self):
        try:
            pick_resize(self.new_size, self.deer_path, self.new_deer_path)
        except AssertionError:
            pass
    
    def test_open_mask_pick(self):
        try:
            pick_resize(self.new_size, self.mask_path, self.new_mask_path)
        except AssertionError:
            pass
        

if __name__=="__main__":
    unittest.main()