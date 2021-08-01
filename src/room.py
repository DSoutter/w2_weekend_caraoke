class Room: 

    def __init__(self, genre, capacity, entry_fee, till):
        self.genre = genre
        self.capacity = capacity
        self.entry_fee = entry_fee
        self.till = till
        self.guests = []
        self.songs = []


    def count_guests(self):
        return len(self.guests)

    def has_capacity(self):
        if self.count_guests()<self.capacity:
            return True
        else:
            return False

    def add_people_to_room(self, guest):
        guest.in_room = self.genre
        self.guests.append(guest)

    def remove_person_from_room(self, guest):
        self.guests.remove(guest)

    def add_song_to_room(self, song):
        self.songs.append(song.name)

# need a method for the guest to remove money
# need a method to increase till if person has money
# also need to check if room has capacity 

    def increase_till(self):
        self.till+=self.entry_fee

    def transaction_occurs(self, guest):
        if self.has_capacity() == False:
            return "No space left I'm afraid"
        elif guest.wallet <= self.entry_fee:
            return "Sorry, not enough money" 
        else:                 
            self.increase_till()
            guest.pay_entry_fee(self)
            self.add_people_to_room(guest)


    