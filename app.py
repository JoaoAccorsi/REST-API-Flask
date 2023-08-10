from flask import Flask
from flask_restful import Resource, Api

# Flask Object
app = Flask(__name__)

# Create the API
api = Api(app)


class Users(Resource):
    # GET HTTP Method
    def get(self):
        return {'message': 'user 1'}   # Return the JSON


class User(Resource):
    def post(self):
        return {'message': 'text'}
    # Get an CPF, and re-direct to one user

    def get(self, cpf):
        return {'message': 'CPF'}


# Add an endpoint for the API created with "api = Api(app)"
api.add_resource(Users, '/users')
api.add_resource(User, '/user', '/user/<string:cpf>')

# If I execute the code by command line, it will execute this
# Add the host to listen outside requests too (container IP) - Do the socket bind in all interfaces, and runs with container IP
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")