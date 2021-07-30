class Room: 

    def __init__(self, genre, capacity, entry_fee, till):
        self.genre = genre
        self.capacity = capacity
        self.entry_fee = entry_fee
        self.till = till
        self.guests = []
        self.songs = []
        