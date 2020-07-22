from src import db

class Collectors(db.Model):

    __tablename__ = 'collectors'


    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), index=True, nullable=False)
    email = db.Column(db.String(64), index=True, nullable=False)


    def __init__(self, name, email):
        self.name = name
        self.email = email


    def __repr__(self):

        return f'Name: {self.name} | Email: {self.email}'








