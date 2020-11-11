from flask_restful import Resource
from flask import request
from app.models import Product, ProductType
from app import db
from ..sessions import *


class ProductResource(Resource):
    def get(self, pk):
        product = Product.query.get_or_404(pk)
        return {"name": product.name, "amount": product.amount}

    def delete(self, pk):
        product = Product.query.get_or_404(pk)
        if product:
            db.session.delete(product)
            result = db.session.commit()
            return result, 200
        return 'No such product', 404


class ProductListResource(Resource):
    def get(self):
        if 'product_type' in request.json:
            product_type = request.json['product_type']

            products_list = db.session.query(Product, ProductType)\
                .join(ProductType)\
                .filter(ProductType.name == product_type).all()

            # TODO: Make better
            return [{"name": i[0].name, "amount": i[0].amount, "sku": i[0].sku} for i in products_list]

        return "No filter", 201

    def post(self):
        name = request.json['name']
        amount = request.json['amount']
        type_name = request.json['product_type']
        sku = request.json['sku']

        product_type = ProductType.query.filter_by(name=type_name).first()

        if product_type:
            pt_res = type_name
        else:
            product_type = ProductType(name=type_name)
            db.session.add(product_type)
            db.session.commit()
            pt_res = f'Product type was created {type_name}'

        product = Product(name=name, amount=amount, sku=sku, type_id=product_type.id)
        db.session.add(product)
        db.session.commit()
        return {"name": product.name, "amount": product.amount, "product_type": pt_res}


class ChangeAmount(Resource):
    def post(self, pk):
        if 'amount' in request.json:
            amount = request.json['amount']
            product = Product.query.get_or_404(pk)
            product.amount += amount
            db.session.commit()
            return {'product': product.name, 'amount': product.amount}

