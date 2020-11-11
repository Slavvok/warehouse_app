from app import create_app, db
from app.views.product import ProductListResource, ProductType, ProductResource, ChangeAmount
import unittest
from app import TestConfig
from flask_restful import Api
from app.sessions import *


class WarehouseTestCase(unittest.TestCase):

    def setUp(self):
        app = create_app(TestConfig)
        api = Api(app)
        api.add_resource(ProductListResource, '/products')
        api.add_resource(ProductResource, '/products/<int:pk>')
        api.add_resource(ChangeAmount, '/products/<int:pk>/change_amount')
        self.app = app.test_client()
        app.app_context().push()
        db.create_all()
        self.create_product()
        db.session.commit()

    def tearDown(self):
        db.drop_all()

    def create_product(self):
        client = self.app.post('/products', json=dict(
            name='product_2',
            amount=5,
            product_type='group_1',
            sku='123asd'
        ))
        self.assertEqual(client.status_code, 200)

    def test_change_product_amount_to_zero(self):
        client = self.app.post('/products/1/change_amount', json=dict(
            amount=-5
        ))
        self.assertEqual(client.status_code, 200)

    def test_change_product_amount_less_than_zero(self):
        client = self.app.post('/products/1/change_amount', json=dict(
            amount=-6
        ))
        self.assertEqual(client.status_code, 400)

    def test_delete_product(self):
        client = self.app.delete('/products/1')
        self.assertEqual(client.status_code, 200)


if __name__ == '__main__':
    unittest.main()