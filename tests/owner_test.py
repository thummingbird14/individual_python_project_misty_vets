import unittest
from models.owner import Owner

class TestOwner(unittest.TestCase):
    
    def setUp(self):
        self.owner = Owner("Louise O'Rourke", "40 East Kilngate Pl", "0131 6661234")
    
    
    def test_owner_has_name(self):
        self.assertEqual("Louise O'Rourke", self.owner.name)
        
        
    def test_owner_has_address(self):
        self.assertEqual("40 East Kilngate Pl", self.owner.address)
       
        
    def test_owner_has_phone_no(self):
        self.assertEqual("0131 6661234", self.owner.phone_no)
    
    
    
   