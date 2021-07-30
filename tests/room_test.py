import unittest

from src.guest import *
from src.room import *
from src.song import *

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room1 = Room("Abba", 8, 50, 1000)
        self.room2 = Room("Christmas", 5, 30, 600)
        self.room3 = Room("Disco", 12, 75, 2000)

        self.guest1 = Guest("Anthony Kiedis", "Abba", 200)
        self.guest2 = Guest("Elton John", "Disco", 150)
        self.guest3 = Guest("Shane MacGowan", "Christmas", 50)



    def test_room1_has_genre(self):
        self.assertEqual("Abba", self.room1.genre)

    def test_room2_has_capacity(self):
        self.assertEqual(5, self.room2.capacity)

    def test_room3_has_entry_fee(self):
        self.assertEqual(75, self.room3.entry_fee)

    def test_room1_has_till(self):
        self.assertEqual(1000, self.room1.till)

    def test_room2_has_no_guests(self):
        self.assertEqual(0,self.room2.count_guests())

    def test_room3_has_enough_capacity(self):
        self.assertEqual(True, self.room3.has_capacity())

# need to add people to the room 
# simple test first for checking in, no money involved.

    def test_room1_does_not_have_enough_capacity(self):
        self.room2.add_people_to_room(self.guest1)
        self.room2.add_people_to_room(self.guest2)
        self.room2.add_people_to_room(self.guest3)
        self.room2.add_people_to_room(self.guest1)
        self.room2.add_people_to_room(self.guest2)
        self.room2.add_people_to_room(self.guest3)
        self.room2.add_people_to_room(self.guest1)
        self.room2.add_people_to_room(self.guest2)
        self.room2.add_people_to_room(self.guest3)

        self.assertEqual(False, self.room2.has_capacity())

    def test_remove_person_from_room3(self):
        self.room3.add_people_to_room(self.guest1)
        self.room3.add_people_to_room(self.guest2)
        self.room3.add_people_to_room(self.guest3)
        self.room3.remove_person_from_room(self.guest1)

        self.assertEqual(2, self.room3.count_guests())