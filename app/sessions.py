from sqlalchemy import event
from sqlalchemy.orm import sessionmaker
from app import db
from .models import Product
from .exceptions import WrongValue


@event.listens_for(Product.amount, 'set', propagate=True)
def check_availability(product, value, initiator, some):
    if value:
        if value < 0:
            raise WrongValue('Final value is less than zero')
    else:
        product.is_available = False

