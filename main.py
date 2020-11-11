from app import app, api
from app.views.product import ProductResource, ProductListResource, ChangeAmount
from flask_restful_swagger import swagger

api.add_resource(ProductListResource, '/products')
api.add_resource(ProductResource, '/products/<int:pk>')
api.add_resource(ChangeAmount, '/products/<int:pk>/change_amount')

if __name__ == "__main__":
    app.run()
