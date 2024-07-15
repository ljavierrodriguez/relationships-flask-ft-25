from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    active = db.Column(db.Boolean, default=True)
    profile = db.relationship('Profile', backref="user", uselist=False)

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "active": self.active,
        }
    
    def serialize_with_profile(self):
        return {
            "id": self.id,
            "username": self.username,
            "active": self.active,
            #"biography": self.profile.biography,
            "profile": self.profile.serialize()
        }

class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    biography = db.Column(db.Text, default="")
    twitter = db.Column(db.Text, default="")
    facebook = db.Column(db.Text, default="")
    instagram = db.Column(db.Text, default="")
    github = db.Column(db.Text, default="")
    linkedin = db.Column(db.Text, default="")
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "biography": self.biography,
            "twitter": self.twitter,
            "facebook": self.facebook,
            "instagram": self.instagram,
            "github": self.github,
            "linkedin": self.linkedin,
            "users_id": self.users_id,
        }