import numpy as np
import pandas as pd

users = [f"user_{i}" for i in range(1, 41)]
names = [
    "Alex", "Ama", "Brian", "Charlotte", "Daniel",
    "David", "Ella", "Emma", "Ethan", "Felicia",
    "Grace", "Hannah", "Isaac", "Jasmine", "Joshua",
    "Kevin", "Linda", "Lucas", "Maria", "Michael",
    "Nathan", "Olivia", "Paul", "Priscilla", "Rachel",
    "Rebecca", "Samuel", "Sarah", "Sophia", "Stephen",
    "Thomas", "Victoria", "William", "Yvonne", "Zoe",
    "Abena", "Kwame", "Akosua", "Kojo", "Nana"
]

songs_genre = {
    "Pop": ["All to well", "Shape of you", "Sue me"],
    "R&B": ["Folded", "Unlearn", "Girls Need Love"],
    "Afrobeats": ["Last Last", "Bout you", "Bounce"],
    "Hip hop": ["Money Trees", "New Flame", "Fair Trade"],
    "Rap": ["Humble", "D1", "Look Alive"],
}

songs = []
for genre in songs_genre:
    songs.extend(songs_genre[genre])


genres = list(songs_genre.keys())
preferred_genres = []
for genre in genres:
    preferred_genres.extend([genre] * 8)

np.random.seed(42)
np.random.shuffle(preferred_genres)

user_preferences = pd.DataFrame({"User": users, "Preferred_genre": preferred_genres})

song_to_genre = {}
for genre in songs_genre:
    for song in songs_genre[genre]:
        song_to_genre[song] = genre

ratings = []
for preference in preferred_genres:
    user_ratings = []

    for song in songs:
        if song_to_genre[song] == preference:
            rating = np.random.randint(4, 6)
        else:
            rating = np.random.randint(1, 4)
        user_ratings.append(rating)
    ratings.append(user_ratings)


ratings = pd.DataFrame(ratings,  columns=songs)
ratings.insert(0,"Name", names)
ratings.insert(0,"UserID", users)

for row in ratings.index:
    unrated_songs = np.random.choice(songs, size=3, replace=False)
    ratings.loc[row, unrated_songs] = 0


ratings.index.name = "User"
ratings.to_csv("user_song_ratings.csv", index=False)
