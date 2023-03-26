from flask import Blueprint
from flask_restful import Api
from resources.school import SchoolResource

api_bp = Blueprint('api/v1.0', __name__)
api = Api(api_bp)

# Route For school endpoints
api.add_resource(SchoolResource, '/school')
# api.add_resource(RestaurantItemResource, '/restaurants/<int:id>')
