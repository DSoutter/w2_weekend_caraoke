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

    def guests_favourite_song(self, song):
        if self.favourite_song == song.name:
            return "I love this song!"
        else:
            return "There are better songs than this"
