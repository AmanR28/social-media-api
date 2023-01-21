from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# Model : Message
class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    message = db.Column(db.String, nullable=False)
    likes = db.Column(db.Integer, default=0)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Message "{self.message}">'
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'message': self.message,
            'likes': self.likes,
            'timestamp': self.timestamp.isoformat()
        }
 
# Model : Likes
class Likes(db.Model):
    message_id = db.Column(
        db.Integer,db.ForeignKey('messages.id'), primary_key=True)
    user_id = db.Column(db.Integer, primary_key=True)