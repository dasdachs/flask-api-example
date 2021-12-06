import datetime

from application import db


class Post(db.Model):
    __tablename__ = "posts"
    pk = db.Column(db.Integer, primary_key=True)
    tile = db.Column(db.String(42), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.now())
    body = db.Column(db.Text)

    def to_json(self):
        return {
            "id": self.pk,
            "title": self.tile,
            "body": self.body,
            "created_at": str(self.created_at)
        }
