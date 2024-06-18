class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artist_count()

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    def add_to_genres(self):
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)

    def add_to_artists(self):
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)

    def add_to_genre_count(self):
        if self.genre not in Song.genre_count:
            Song.genre_count[self.genre] = 0
        Song.genre_count[self.genre] += 1

    def add_to_artist_count(self):
        if self.artist not in Song.artist_count:
            Song.artist_count[self.artist] = 0
        Song.artist_count[self.artist] += 1

    @classmethod
    def get_artists(cls):
        return Song.artists.copy()

    @classmethod
    def get_genres(cls):
        return Song.genres.copy()

    @classmethod
    def get_genre_count(cls):
        return Song.genre_count.copy()

    @classmethod
    def get_artist_count(cls):
        return Song.artist_count.copy()

# Example usage:
ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
single_ladies = Song("Single Ladies", "Beyonce", "Pop")
hotline_bling = Song("Hotline Bling", "Drake", "Rap")

print(Song.count)  # Output: 3
print(Song.get_artists())  # Output: ['Jay-Z', 'Beyonce', 'Drake']
print(Song.get_genres())  # Output: ['Rap', 'Pop']
print(Song.get_genre_count())  # Output: {'Rap': 2, 'Pop': 1}
print(Song.get_artist_count())  # Output: {'Jay-Z': 1, 'Beyonce': 1, 'Drake': 1}
