from flask import Flask
from flask.ext.restplus import Api, Resource, fields


info = """
This API defines the rsources and actions to manage a virtual cluster on the
SDSC comet cluster."""

app = Flask(__name__)
api = Api(app,
          version='1.0.2',
          title='Virtual Cluster API',
          description=info
          )

ns_cluster = api.namespace('cluster', 'Cluster commands')
ns_project = api.namespace('project', 'Project commands')
ns_user = api.namespace('user', 'User commands')

@ns_cluster.route('/')
class Clusters(Resource):
    """
    ids
    """
    @api.response(200, 'Success')
    @api.response(400, 'Validation Error')
    def get(self):
        return {'clusters': 'to be implemented'}

    def post(self):
        return {'cluster': 'get to be implemented'}

@ns_cluster.route('/<string:id>')
@api.doc(params={'id': 'The unique id of the cluster'})
class Cluster(Resource):
    """
    id
    """
    def get(self, id):
        return {'cluster': 'get to be implemented'}
    
    def delete(self, id):
        return {'cluster': 'delete to be implemented'}


@ns_project.route('/')
@api.doc(params={'name': 'The unique name of the project'})
class Projects(Resource):
    def get(self, name):
        return {'projects': 'get to be implemented'}


@ns_project.route('/<string:name>')
@api.doc(params={'name': 'The unique name of the project'})
class Project(Resource):
    """
    name
    """
    def get(self, name):
        return {'project': 'get to be implemented'}

    def post(self):
        return {'Project': 'get to be implemented'}
    
    def delete(self, name):
        return {'Project': 'delete to be implemented'}

@ns_user.route('/')    
class Users(Resource):
    def get(self):
        return {'Users': 'get to be implemented'}

    
@ns_user.route('/<string:username>')
@api.doc(params={'username': 'The unique username'})
class User(Resource):
    """
    firstname
    lastname
    email
    username
    """
    
    def get(self, username):
        return {'User': 'get to be implemented'}

    def post(self):
        return {'User': 'get to be implemented'}
    
    def delete(self, username):
        return {'cluster': 'delete to be implemented'}
    
if __name__ == '__main__':
    app.run(debug=True)
