import unittest

from src.guest import *
from src.room import *
from src.song import *

class TestSong(unittest.TestCase):

    def setUp(self):
        self.genre1 = "Pop"
        self.genre2 = "Christmas"
        self.genre3 = "Disco"

        self.room1 = Room(self.genre1, 8, 50, 1000)
        self.room2 = Room(self.genre2, 5, 30, 600)
        self.room3 = Room(self.genre3, 12, 75, 2000)

        self.guest1 = Guest("Anthony Kiedis", "Abba", 200)
        self.guest2 = Guest("Elton John", "Disco", 150)
        self.guest3 = Guest("Shane MacGowan", "Christmas", 50)

        self.song1 = Song("Mamma Mia","Abba",self.genre1)
        self.song2 = Song("22","Taylor Swift",self.genre1)
        self.song3 = Song("Uptown Funk","Mark Ronson",self.genre1)
        self.song4 = Song("Fairytale of New York","The Pogues",self.genre2)
        self.song5 = Song("All I want for Christmas is You","Mariah Carey",self.genre2)
        self.song6 = Song("Christmas Time","The Darkness",self.genre2)
        self.song7 = Song("Y.M.C.A","The Village People",self.genre3)
        self.song8 = Song("Night Fever","Bee Gees",self.genre3)
        self.song9 = Song("Funky Town","Lipps Inc",self.genre3)

    def test_song1_has_name(self):
        self.assertEqual("Mamma Mia", self.song1.name)

    def test_song2_has_artist(self):
        self.assertEqual("Taylor Swift", self.song2.artist)

    def test_song3_has_genre(self):
        self.assertEqual("Pop", self.song3.genre)
