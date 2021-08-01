class Guest:

    def __init__(self, name, favourite_genre, favourite_song, wallet):
        self.name = name
        self.favourite_genre = favourite_genre
        self.favourite_song = favourite_song
        self.wallet = wallet
        self.in_room = ""

    def what_room_guest_is_in(self,room):
        self.in_room = room.genre
        return self.in_room

    def guest_in_favourite_room(self, room):
        if self.in_room == self.favourite_genre:
            return f"{self.in_room} Karaoke is {self.name}'s favourite genre!" 
        else:
            return f"{self.in_room} Karaoke is NOT {self.name}'s favourite genre!"

    def guests_favourite_song(self, room):
        if self.favourite_song in room.songs:
            return "This room's playing my song!"
        else:
            return "They should get some better songs..."

    def pay_entry_fee(self, room):
        self.wallet -= room.entry_fee