class Guest:

    def __init__(self, name, favourite_genre, wallet):
        self.name = name
        self.favourite_genre = favourite_genre
        self.wallet = wallet
        self.in_room = ""

    def what_room_guest_is_in(self,room):
        self.in_room = room.genre
        return self.in_room

    def guest_in_favourite_room(self, room):
        if self.in_room == self.favourite_genre:
            return True
        else:
            return False
