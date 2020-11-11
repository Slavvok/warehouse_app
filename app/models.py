from app import Config, db
from sqlalchemy.orm import relationship


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    amount = db.Column(db.Integer)
    sku = db.Column(db.String(20), unique=True)
    is_available = db.Column(db.Boolean, default=True)
    type_id = db.Column(db.Integer, db.ForeignKey('product_type.id'))

    product_type = relationship("ProductType")

    # def __repr__(self):
    #     return f'{self.id} {self.name} {self.amount}'


class ProductType(db.Model):
    __tablename__ = 'product_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)


# class ProductHistory(db.Model):
#     __tablename__ = 'product_history'
#     product_id = db.Column(db.Integer, db.ForeignKey('product_history.id'))
#     value_before = db.Column(db.Integer)
#     value_after = db.Column(db.Integer)
