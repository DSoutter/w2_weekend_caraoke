import unittest

from src.guest import *
from src.room import *
from src.song import *

#have 3 rooms
#have 3 guests
#have 3 songs (to start)

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.room1 = Room("Abba", 8, 50, 1000)
        self.room2 = Room("Christmas", 5, 30, 600)
        self.room3 = Room("Disco", 12, 75, 2000)

        self.guest1 = Guest("Anthony Kiedis", "Abba", 200)
        self.guest2 = Guest("Elton John", "Disco", 150)
        self.guest3 = Guest("Shane MacGowan", "Christmas", 50)

    def test_what_room_guest_is_in(self):
        self.room1.add_people_to_room(self.guest1)
        self.assertEqual("Abba", self.guest1.what_room_guest_is_in(self.room1))

    def test_guest_in_favourite_room(self):
        self.room2.add_people_to_room(self.guest3)
        self.assertEqual(True, self.guest3.guest_in_favourite_room(self.room2))