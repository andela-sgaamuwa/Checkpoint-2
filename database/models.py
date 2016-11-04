from app import app, db
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)

class User(db.Model):
    """User Database class
    This class defines database fields for the users of the system
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(250), nullable=False)
    password_hash = db.Column(db.String(250))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_auth_token(self, expires_in=1800):
        s = Serializer(app.config["samuel"], expires_in=expires_in)
        return s.dumps({"id": self.id}).decode("utf-8")
    
    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None
        return User.query.get(data['id'])
        

class Bucketlist(db.Model):
    """Bucketlist Database class
    This class defines database fields for the bucketlists
    """
    __tablename__ = 'bucketlist'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(250), nullable=False)
    date_created = db.Column(db.DateTime(True), nullable=False)
    date_modified = db.Column(db.DateTime(True), nullable=True)
    created_by = db.Column(db.String(250), nullable=False)

class Item(db.Model):
    """Item Database class
    This class defines database fields for the items in the bucketlists
    """
    __tablename__ = 'item'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(250), nullable=False)
    date_created = db.Column(db.DateTime(True), nullable=False)
    date_modified = db.Column(db.DateTime(True), nullable=True)
    done = db.Column(db.Boolean, nullable=False)

db.create_all()