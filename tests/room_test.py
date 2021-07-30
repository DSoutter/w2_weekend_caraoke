import unittest

from src.guest import *
from src.room import *
from src.song import *

class TestRoom(unittest.TestCase):

        def setUp(self):
            self.room1 = Room("Abba", 10, 50, 1000)
            self.room2 = Room("Christmas", 5, 30, 600)
            self.room3 = Room("Disco", 20, 75, 2000)

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