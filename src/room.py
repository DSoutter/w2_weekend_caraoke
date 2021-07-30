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
        self.guests.append(guest)