from flask import Flask
from flask.ext.restplus import Api, Resource, fields

info = """
This API defines the rsources and actions to manage a virtual cluster
on the SDSC comet cluster.

We are defining as part of this API a number of collections that
contain a group of resources of a particular resource. This includes:

* Clusters
* Users
* Projects

Other storage related  will be added. Each of them will support

A **Collection** is a group of Resources of a given type. The
following methods are supported:
 
* A **GET** request retrieves a list of summarized Resource
  representations This summary *may* include all or some of the
  Resource properties but *must* include a link to the full
  Resource representation.

* A **POST** request will create a new Resource in the Collection.
  The set of Resource properties *must* be specified as a JSON
  object in the request body.

A **Resource** is a representation of a singular object in the API 

* A **GET** request retrieves the full Resource representation.

* A **DELETE** request will delete the Resource. This request
    *may* contain a JSON object which specifies optional parameters.

* (**Comment:** We may want o do all modifications via a POST?) A **PUT**
    request is used to modify the properties of a Resource (eg. Change
    the name of a Virtual Machine). This kind of request *must not*
    alter the live state of the Resource. Only *actions* may alter
    live state.

*  A **POST** request commits an *action* upon a Resource (eg.
    Start a Virtual Machine). This request is made to a URI relative
    to the Resource URI. Available *actions* are described within
    the *actions* property of a Resource representation. The request
    body *must* contain a JSON object which specifies parameters.

**Comments:**

* use **PATCH** for changing a subset of values of an exsiting resource.
"""

app = Flask(__name__)
api = Api(app,
          version='1.0.2',
          title='Virtual Cluster API',
          description=info
          )

# #####################################################################
# Namespaces
# #####################################################################

ns_cluster = api.namespace('cluster', 'Cluster commands')
ns_project = api.namespace('project', 'Project commands')
ns_user = api.namespace('user', 'User commands')

# #####################################################################
# Models
# #####################################################################

model_compute = api.model('ComputeModel', {
    'name': fields.String(required=True,
                          description="unique name of the compute resource"),
    'internal_ip': fields.String(description="internal ip of the compute resource"),
    'external_ip': fields.String(description="external ip of the compute resource"),
    'username': fields.String(description="username who is controlling this compute resource"),   
    'project': fields.String(description="project the compute resource belongs to"),        
})

model_manager = api.model('ComputeModel', {
    'name': fields.String(required=True,
                          description="unique name of the compute resource"),
    'internal_ip': fields.String(description="internal ip of the compute resource"),
    'external_ip': fields.String(description="external ip of the compute resource"),
    'username': fields.String(description="username who is controlling this compute resource"),   
    'project': fields.String(description="project the compute resource belongs to"),        
})

model_cluster = api.model('ClusterModel', {
    'name': fields.String(required=True,
                          description="unique name of the compute cluster"),
    'management': fields.Nested(model_manager, description='The manager'),
    'compute': fields.List(fields.Nested(model_compute))
})

listed_todo = api.model('ListedTodo', {
    'id': fields.String(required=True, description='The todo ID'),

})


model_project = api.model('ProjectModel', {
    'name': fields.String(required=True,
                          description="project name")
})

model_user = api.model('UserModel', {
    'username': fields.String(required=True,
                              description="uniqe username of the user"),
    'firstname': fields.String(required=True,
                               description="first name of the user"),
    'lastname': fields.String(required=True,
                              description="lastname of the user"),
    'email': fields.String(required=True,
                           description="email of the user"),
})

# #####################################################################
# Clusters
# #####################################################################

@ns_cluster.route('/')
class Clusters(Resource):
    """
    Management of a list of clusters.
    """
    @api.response(200, 'Success')
    @api.response(400, 'Validation Error')
    def get(self):
        """
        Obtaining the list of custers.
        The names of the clusters will be returned.
        """
        return {'clusters': 'to be implemented'}

    def post(self):
        """Create a new cluster."""
        return {'cluster': 'post to be implemented'}

@ns_cluster.route('/<string:id>')
@api.doc(params={'id': 'The unique id of the cluster'})
class Cluster(Resource):
    """
    id
    """
    def get(self, id):
        """Get a cluster by unique id."""
        return {'cluster': 'get to be implemented'}
    
    def delete(self, id):
        """Get a cluster by unique id."""            
        return {'cluster': 'delete to be implemented'}

# #####################################################################
# Projects
# #####################################################################

@ns_project.route('/')
@api.doc(params={'name': 'The unique name of the project'})
class Projects(Resource):
    def get(self):
        """Get the list of project names."""            
        return {'projects': 'get to be implemented'}

    def post(self):
        """Create a new project with a unique id"""
        return {'Project': 'post to be implemented'}
    

@ns_project.route('/<string:name>')
@api.doc(params={'name': 'The unique name of the project'})
class Project(Resource):
    """
    name
    """
    def get(self, name):
       """Get a project by unique id."""
       return {'project': 'get to be implemented'}

    def delete(self, name):
        """Delete a project by unique id."""
        return {'Project': 'delete to be implemented'}

# #####################################################################
# Users
# #####################################################################

user_parser = api.parser()
user_parser.add_argument('username',
                         type=str,
                         required=True,
                         help='The username', location='form')
user_parser.add_argument('firstname',
                         type=str,
                         required=True,
                         help='The firstname', location='form')
user_parser.add_argument('lastname',
                         type=str,
                         required=True,
                         help='The lastname', location='form')
user_parser.add_argument('email',
                         type=str,
                         required=True,
                         help='The email', location='form')


@ns_user.route('/')    
class Users(Resource):
    def get(self):
        """Get the list of users"""
        return {'Users': 'get to be implemented'}

    def post(self):
        '''Create a user'''
        args = user_parser.parse_args()
        print (args)
        return args['username'], 201
        # return {'User': 'post to be implemented'}
    
    def patch(self):
    	"""test if patch is available"""
        return {'User': 'post to be implemented'}
    
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
        """Get user by unique user name."""
        return {'User': 'get to be implemented'}

    def delete(self, username):
        """Delete a user by unique user name."""
        return {'cluster': 'delete to be implemented'}

# #####################################################################
# Main
# #####################################################################

if __name__ == '__main__':
    app.run(debug=True)
