from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Cluster
from .models import ClusterSerializer


# from api.models import User
# from api.serializers import UserSerializer

# from api.models import Project
# from api.serializers import ProjectSerializer

# from api.models import Storagepool
# from api.serializers import StoragepoolSerializer

# @api_view(['GET'])
# def cluster_list(request):
#    return Response("response")

class UserList(APIView):
    """
    List all Persons that can create clusters.
    We will investigate djangos build in classes for that.
    """
    def get(self, request, format=None):
        return Response("todo")
        
    def post(self, request, format=None):
        return Response("todo")

class ProjectList(APIView):
    """
    List all Projects that can create clusters.
    We will investigate if django has already a project as part of user management.
    """
    def get(self, request, format=None):
        return Response("todo")
        
    def post(self, request, format=None):
        return Response("todo")

class ProjectDetail(APIView):
    """
    Retrieve, update or delete a project instance.
    """
    def get_object(self, id):
        # try:
        #    return Project.objects.get(id=id)
        # except Project.DoesNotExist:
        #    raise Http404
        return None

    def get(self, request, id, format=None):
        # project = self.get_object(id)
        # serializer = ProjectSerializer(project)
        # return Response(serializer.data)
        return Response("todo")
    
    def put(self, request, id, format=None):
        # project = self.get_object(id)
        # serializer = ProjectSerializer(project, data=request.data)
        # if serializer.is_valid():
        #    serializer.save()
        #    return Response(serializer.data)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("todo")
        
    def delete(self, request, id, format=None):
        # project = self.get_object(id)
        # project.delete()
        # return Response(status=status.HTTP_204_NO_CONTENT)
        return Response("todo")
        
class UserDetail(APIView):
    """
    Retrieve, update or delete a user instance.
    """
    def get_object(self, id):
        # try:
        #    return User.objects.get(id=id)
        # except User.DoesNotExist:
        #    raise Http404
        return None

    def get(self, request, id, format=None):
        # user = self.get_object(id)
        # serializer = UserSerializer(user)
        # return Response(serializer.data)
        return Response("todo")
    
    def put(self, request, id, format=None):
        # user = self.get_object(id)
        # serializer = UserSerializer(user, data=request.data)
        # if serializer.is_valid():
        #    serializer.save()
        #    return Response(serializer.data)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("todo")
        
    def delete(self, request, id, format=None):
        # user = self.get_object(id)
        # user.delete()
        # return Response(status=status.HTTP_204_NO_CONTENT)
        return Response("todo")
        
class ClusterList(APIView):
    """
    List all clusters, or create a new cluster.
    """
    def get(self, request, format=None):
        clusters = Cluster.objects.all()
        serializer = CLusterSerializer(clusters, many=True)
        return Response(serializer.data)
        
    def post(self, request, format=None):
        serializer = ClusterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClusterDetail(APIView):
    """
    Retrieve, update or delete a cluster instance.
    """
    def get_object(self, id):
        try:
           return Cluster.objects.get(id=id)
        except Cluster.DoesNotExist:
           raise Http404

    def get(self, request, id, format=None):
        cluster = self.get_object(id)
        serializer = ClusterSerializer(cluster)
        return Response(serializer.data)
    
    def put(self, request, id, format=None):
        cluster = self.get_object(id)
        serializer = ClusterSerializer(cluster, data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id, format=None):
        cluster = self.get_object(id)
        cluster.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
@api_view(['POST'])
def cluster_start(request, cluster_name):
    return Response("response cluster start")

@api_view(['POST'])
def cluster_stop(request, cluster_name):
    return Response("response cluster stop")

