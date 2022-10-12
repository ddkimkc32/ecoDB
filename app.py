# from flask import Flask, render_template, request

import db
from db import addUser


from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin


# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)




# making a class for a particular resource
# the get, post methods correspond to get and post requests
# they are automatically mapped by flask_restful.
# other methods include put, delete, etc.

class User(Resource):

    # corresponds to the GET request.
    # this function is called whenever there
    # is a GET request for this resource
    def get(self):
        
        return jsonify({'message': 'hello world'})

    # Corresponds to POST request
    def post(self):
        data = request.get_json()
        db.addUser(data['username'], data['password'], data['email'])
        return restful.request.form, 201, {'Access-Control-Allow-Origin': '*'} 
    def options (self):
        return {'Allow' : 'PUT' }, 200, \
            { 'Access-Control-Allow-Origin': '*', \
              'Access-Control-Allow-Methods' : 'PUT,GET' 
            }


# another resource to calculate the square of a number


# adding the defined resources along with their corresponding urls
api.add_resource(User, '/register')


# driver function
if __name__ == '__main__':

    app.run(debug = True)
