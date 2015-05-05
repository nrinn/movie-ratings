"""Utility file to seed ratings database from MovieLens data in seed_data/"""

from model import User, Rating, Movie, connect_to_db, db
from server import app
from datetime import datetime

def load_users():
    """Load users from u.user into database."""
    f = open("seed_data/u.user")
    for line in f:
        line = line.rstrip().split("|")
        user_id = line[0]
        age = line[1]
        zipcode = line[4]

        user = User(user_id=user_id, age=age, zipcode=zipcode)
 
        db.session.add(user)

    db.session.commit()

def load_movies():
    """Load movies from u.item into database."""
    m = open("seed_data/u.item")
    for line in m:
        line = line.rstrip().split("|")
        movie_id = line[0]
        title_and_year = line[1]
        title_splitted = title_and_year.split()
        title = " ".join(title_splitted[:-1])
        imdb_url = line[4]
        s = line[2]
        if not s:
            released_at = datetime.now()
        else:
            released_at = datetime.strptime(s,"%d-%b-%Y")

            movie = Movie(movie_id=movie_id, title=title, released_at=released_at, imdb_url=imdb_url)

            db.session.add(movie)
        db.session.commit()


def load_ratings():
    """Load ratings from u.data into database."""
    r = open("seed_data/u.data")
    for line in r:
        line = line.split()
        movie_id = int(line[1])
        user_id = int(line[0])
        score = int(line[2]) 

        rating = Rating(movie_id=movie_id, user_id=user_id, score=score)
        db.session.add(rating)

    db.session.commit()

if __name__ == "__main__":
    connect_to_db(app)

    load_users()
    load_movies()
    load_ratings()
