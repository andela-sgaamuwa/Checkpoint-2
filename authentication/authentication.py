from database.models import User
from app import db


class Authentication(object):
    """Authentication class
    
    The authentication class is used to manage users of the System 
    Users can be registered with a username and password and added to 
    the database
    Logs in users into the system
    """

    def register_user(user_data):
        """registers and adds new users the database"""
        user = User(username=user_data['username'])
        # give the user password a hash value and store it
        user.set_password(password=user_data['password'])
        if user in User.query.filter_by(username=user_data['username']):
            status = "success"
        try:
            db.session.add(user)
            db.session.commit()
            status = 'success'
        except:
            status = 'this user is already registered'
        db.session.close()
        return status

    def login_user(user_data):
        """logs in users to the System
        returns an error if the credentials are not valid
        """
        user = User.query.filter_by(username=user_data['username']).first()
        # check if the user and password exist and are right 
        if user and user.verify_password(user_data['password']):
            return True
        else:
            return False
        
    def verify_user(username, password):
        """checks if a user exists and verifies their password"""
        user = User.query.filter_by(username=username).first()
        if not user or not user.verify_password(password):
            return False
        return user

    def verify_token(token):
        """verifies tokens used in the system for access"""
        user = User.verify_auth_token(token)
        return user is not None