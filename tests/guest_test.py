import unittest

from src.guest import *
from src.room import *
from src.song import *

#have 3 rooms
#have 3 guests
#have 3 songs (to start)

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.genre1 = "Pop"
        self.genre2 = "Christmas"
        self.genre3 = "Disco"

        self.room1 = Room(self.genre1, 8, 50, 1000)
        self.room2 = Room(self.genre2, 5, 30, 600)
        self.room3 = Room(self.genre3, 12, 75, 2000)

        self.guest1 = Guest("Anthony Kiedis", "Abba", "Mamma Mia", 200)
        self.guest2 = Guest("Elton John", "Disco", "Funky Town", 150)
        self.guest3 = Guest("Shane MacGowan", "Christmas", "Fairytale of New York",  50)

        self.song1 = Song("Mamma Mia","Abba",self.genre1)
        self.song2 = Song("22","Taylor Swift",self.genre1)
        self.song3 = Song("Uptown Funk","Mark Ronson",self.genre1)
        self.song4 = Song("Fairytale of New York","The Pogues",self.genre2)
        self.song5 = Song("All I want for Christmas is You","Mariah Carey",self.genre2)
        self.song6 = Song("Christmas Time","The Darkness",self.genre2)
        self.song7 = Song("Y.M.C.A","The Village People",self.genre3)
        self.song8 = Song("Night Fever","Bee Gees",self.genre3)
        self.song9 = Song("Funky Town","Lipps Inc",self.genre3)


    def test_what_room_guest_is_in(self):
        self.room1.add_people_to_room(self.guest1)
        self.assertEqual("Pop", self.guest1.what_room_guest_is_in(self.room1))

    def test_guest_in_favourite_room_true(self):
        self.room2.add_people_to_room(self.guest3)
        self.assertEqual("Christmas Karaoke is Shane MacGowan's favourite genre!", self.guest3.guest_in_favourite_room(self.room2))

    def test_guest_in_favourite_room_false(self):
        self.room1.add_people_to_room(self.guest3)
        self.assertEqual("Pop Karaoke is NOT Shane MacGowan's favourite genre!", self.guest3.guest_in_favourite_room(self.room2))

    def test_guests_favourite_song_in_room_true(self):
        self.room1.add_song_to_room(self.song1)
        self.room1.add_song_to_room(self.song2)
        self.room1.add_song_to_room(self.song3)

        self.assertEqual("I love this song!", self.guest1.guests_favourite_song(self.song1))
                