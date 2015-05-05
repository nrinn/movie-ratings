"""Utility file to seed ratings database from MovieLens data in seed_data/"""

from model import User, Rating, Movie, connect_to_db, db
from server import app


def load_users():
    """Load users from u.user into database."""
    # import u.user
    # connection = sqlite3.connect('ratings.db')
    f = open("seed_data/u.user")
    for line in f:
        line = line.rstrip().split("|")
        newuser = User(user_id = line[0], age = line[1], zipcode = line[4])

        db.session.add(newuser)

        # user_id = line[0] 
        # age = line[1]
        # zipcode = line[4]
        # db.session.add(User)
        
        # db.session.add(user)


        # email = "NULL"
        # password = "NULL"

        # print "HIIIIIII!!!!!"
        # print user_id, email, zipcode 

    # QUERY = "INSERT INTO users VALUES(user_id, email, password, age, zipcode)"
    # connect.commit() 




def load_movies():
    """Load movies from u.item into database."""


def load_ratings():
    """Load ratings from u.data into database."""


if __name__ == "__main__":
    connect_to_db(app)

    load_users()
    # load_movies()
    # load_ratings()
