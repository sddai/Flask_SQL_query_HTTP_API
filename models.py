from app import db


class Identifier(db.Model):
    # See http://flask-sqlalchemy.pocoo.org/2.0/models/#simple-example
    # for details on the column types.

    # We always need an id
    id = db.Column(db.Integer, primary_key=True)

    # A dessert has a name, a price and some calories:
    identifier = db.Column(db.String(100))
    price = db.Column(db.String(100))
    info = db.Column(db.String(1000))

    def __init__(self, identifier, price, info):
        self.identifier = identifier
        self.price = price
        self.info = info

    def calories_per_dollar(self):
        if self.info:
            return self.info / self.price

    # def to_json(self):
    #     json_dict = self.__dict__
    #     if "_sa_instance_state" in json_dict:
    #         del json_dict["_sa_instance_state"]
    #     return json_dict


class Menu(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    identifier = db.Column(db.String(100))

    def __init__(self, name):
        self.identifier = name


def create_dessert(new_identifier, new_price, new_info):
    # Create a dessert with the provided input.
    # At first, we will trust the user.

    # This line maps to line 16 above (the Dessert.__init__ method)
    dessert = Identifier(new_identifier, new_price, new_info)

    # Actually add this dessert to the database
    db.session.add(dessert)

    # Save all pending changes to the database
    db.session.commit()

    return dessert


if __name__ == "__main__":

    # Run this file directly to create the database tables.
    print "Creating database tables..."
    db.create_all()
    print "Done!"
