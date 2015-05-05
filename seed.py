"""Utility file to seed ratings database from MovieLens data in seed_data/"""

from model import User, Rating, Movie, connect_to_db, db
from server import app
from datetime import datetime

# def load_users():
#     """Load users from u.user into database."""
#     # import u.user
#     # connection = sqlite3.connect('ratings.db')
#     f = open("seed_data/u.user")
#     for line in f:
#         line = line.rstrip().split("|")
#         user_id = line[0]
#         age = line[1]
#         zipcode = line[4]

#         user = User(user_id=user_id, age=age, zipcode=zipcode)
 
#         db.session.add(user)
#     db.session.commit()  
       

def load_movies():
    """Load movies from u.item into database."""
    m = open("seed_data/u.item")
    for line in m:
        line = line.rstrip().split("|")
        movie_id = line[0]
        title_and_year = line[1]
        title_in_two = title_and_year.split("(")
        title = title_in_two[0]
        imdb_url = line[4]
        s = line[2]
        if not s:
            released_at = datetime.now()
        else:
            released_at = datetime.strptime(s,"%d-%b-%Y")
       

        print released_at

def load_ratings():
    """Load ratings from u.data into database."""


if __name__ == "__main__":
    connect_to_db(app)

    # load_users()
    load_movies()
    # load_ratings()
