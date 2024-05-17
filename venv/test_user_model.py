"""User model tests."""

# run these tests like:
#
#    python -m unittest test_user_model.py


import os
from unittest import TestCase

from models import db, connect_db, User, Message, Likes, Follows

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database

os.environ['DATABASE_URL'] = "postgresql://postgres:pepe1@localhost/warbler_test"


# Now we can import app

from app import app

# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

db.drop_all()
db.create_all()


class UserModelTestCase(TestCase):
    """Test views for messages."""

    # def setUp(self):
    #     """Create test client, add sample data."""

    #     # User.query.delete()
    #     # Message.query.delete()
    #     # Follows.query.delete()

    #     self.client = app.test_client()

    # # def test_user_model(self):
    # #     """Does basic model work?"""

    # #     # u = User(
    # #     #     email="test@test.com",
    # #     #     username="testuser",
    # #     #     password="HASHED_PASSWORD"
    # #     # )

    # #     # db.session.add(u)
    # #     # db.session.commit()

    # #     # User should have no messages & no followers
    # #     self.assertEqual(len(u.messages), 0)
    # #     self.assertEqual(len(u.followers), 0)
        
   
    def User_test(self):
        u = User(
        email="test@test.com",
        username="testuser",
        password="HASHED_PASSWORD" )
        db.session.add(u)
        db.session.commit()
                 
        Test_client = User.query.get(u.id)
        assert Test_client.email == "test@test.com"
        assert Test_client.username == "testuseeer"
                
    def test_user_model_id_autoincrements(self):
         user1 = User( email="test@test.com",
             username="testuser",
             password="HASHED_PASSWORD")
         db.session.add(user1)
         db.session.commit()
     
         user2 = User( email="test@test2.com",
             username="testuser2",
             password="HASHED_PASSWORD")
         db.session.add(user2)
         db.session.commit()
     
         fetched_playlist1 = User.query.get(user1.id)
         fetched_playlist2 = User.query.get(user2.id)
         assert fetched_playlist1.id < fetched_playlist2.id