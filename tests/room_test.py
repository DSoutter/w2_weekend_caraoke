import unittest

from src.guest import *
from src.room import *
from src.song import *
from src.bar import *

class TestRoom(unittest.TestCase):

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

        self.drink1 = Bar("Beer", 100, 10)
        self.drink2 = Bar("Wine", 50, 8)
        self.drink3 = Bar("Vodka", 25, 5)

    def test_room1_has_genre(self):
        self.assertEqual("Pop", self.room1.genre)

    def test_room2_has_capacity(self):
        self.assertEqual(5, self.room2.capacity)

    def test_room3_has_entry_fee(self):
        self.assertEqual(75, self.room3.entry_fee)

    def test_room1_has_till(self):
        self.assertEqual(1000, self.room1.till)

    def test_room2_has_no_guests(self):
        self.assertEqual(0,self.room2.count_guests())

    def test_room3_has_enough_capacity_True(self):
        self.assertEqual(True, self.room3.has_capacity())

# need to add people to the room 
# simple test first for checking in, no money involved.

    def test_room1_does_not_have_enough_capacity_False(self):
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

    def test_song4_is_in_room2_true(self):
        self.room2.add_song_to_room(self.song4)
        self.assertEqual(True, self.song4.name in self.room2.songs)

    def test_song4_is_in_room2_false(self):
        self.assertEqual(False, self.song4 in self.room2.songs)

    def test_entry_fee_being_paid(self):
        self.room2.transaction_occurs(self.guest2)

        self.assertEqual(630, self.room2.till)
        self.assertEqual(120, self.guest2.wallet)


    def test_entry_fee_not_paid_no_space(self):
        self.room2.add_people_to_room(self.guest1)
        self.room2.add_people_to_room(self.guest2)
        self.room2.add_people_to_room(self.guest3)
        self.room2.add_people_to_room(self.guest1)
        self.room2.add_people_to_room(self.guest2)
        
        outcome = self.room2.transaction_occurs(self.guest3)

        self.assertEqual("No space left I'm afraid", outcome)

    def test_entry_not_allowed_no_money(self):

        outcome = self.room3.transaction_occurs(self.guest3)

        self.assertEqual("Sorry, not enough money", outcome)

    def test_full_entry_successful(self):
        self.room1.transaction_occurs(self.guest1)

        self.assertEqual(1050, self.room1.till)
        self.assertEqual(150, self.guest1.wallet)
        self.assertEqual(1, self.room1.count_guests())

# to buy drink, customer has to have money
# bar has to sell the drink, quantity goes down
# bar till goes up
# wallet goes down
# guest adds to list of drinks had
# bar tracks guests spending

    def test_check_bar_tab(self):
        self.room2.create_bar_tab(self.guest1)

        self.assertEqual({"Anthony Kiedis" : 30}, self.room2.bar_tab)

    def test_guest_bought_drink(self):
        self.room2.transaction_occurs(self.guest1)
        self.room2.create_bar_tab(self.guest1)
        self.room2.sell_drink(self.guest1, self.drink1)
    
        self.assertEqual(730, self.room2.till)
        self.assertEqual(70, self.guest1.wallet)
        self.assertEqual({"Anthony Kiedis" : 130},self.room2.bar_tab )
        self.assertEqual(["Beer"],self.guest1.drinks_had)
        self.assertEqual(9, self.drink1.quantity)

    def test_guest_bought_multiple_drinks(self):
        self.room2.transaction_occurs(self.guest2)
        self.room2.create_bar_tab(self.guest2)
        self.room2.sell_drink(self.guest2, self.drink2)
        self.room2.sell_drink(self.guest2, self.drink3)
                
                
        self.assertEqual(705, self.room2.till)
        self.assertEqual({"Elton John" : 105},self.room2.bar_tab)
        self.assertEqual(["Wine","Vodka"],self.guest2.drinks_had)
        self.assertEqual(7, self.drink2.quantity)
        self.assertEqual(4, self.drink3.quantity)
    # def test_two_guests_bought_drink(self):
