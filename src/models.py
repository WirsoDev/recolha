from src import db


class Collectors(db.Model):


    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), index=True, nullable=False)
    email = db.Column(db.String(64), index=True, nullable=False)
    adress = db.Column(db.String(64), index=True, nullable=False)
    adress2 = db.Column(db.String(64))
    number = db.Column(db.Integer, index=True, nullable=False)
    district = db.Column(db.String(64), index=True, nullable=False)
    city = db.Column(db.String(64), nullable=False)
    itens = db.Column(db.Text, nullable=False)


    def init(self, name, email, adress, adress2, number, district, city, itens):

        self.name = name
        self.email = email
        self.adress = adress
        self.adress2 = adress2
        self.number = number
        self.district = district
        self.city = city
        self.itens = itens

    def repr(self):

        return f'ID: {self.id} Name: {self.name} | Email: {self.email} | City: {self.city}'
