
from urllib import response
import db, postdb
from db import addUser
from postdb import addPosts
from flask import Flask, jsonify, request, Response
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
import logging
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)


class User(Resource):
    # corresponds to the GET request.
    def get(self):
        return jsonify({'message': 'hello world'})
    # Corresponds to POST request
    def post(self):
        print(request)
        data = request.get_json()
        print(data)
        db.addUser(data["username"], data["password"], data["email"])
        return({'Access-Control-Allow-Origin': "*"})
    def options (self):
        return(
            
             {'Allow' : 'PUT' }, 200, \
            { 'Access-Control-Allow-Origin': "*", \
              'Access-Control-Allow-Methods' : 'PUT,GET', \
              "Access-Control-Allow-Headers" : "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
            })
            


class Post(Resource):
    def get(self):
        # return getPosts
        return
    def post(self):
        data = request.get_json()
        postdb.addPosts(data["username"], data["content"], data["date"])
        return jsonify({
            "message": "Success"
        })

# adding the defined resources along with their corresponding urls
api.add_resource(User, '/register')

api.add_resource(Post, '/post')

# driver function
if __name__ == '__main__':

    app.run(debug= True)
