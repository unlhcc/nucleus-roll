from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import detail_route
from models import *


class ClusterViewSet(ModelViewSet):
    lookup_field = 'cluster_id'
    serializer_class = ClusterSerializer

    def list(self, request, format=None):
        #clusters = Cluster.objects.all()
        #serializer = CLusterSerializer(clusters, many=True)
        #return Response(serializer.data)
        return Response("todo")

    def retrieve(self, request, cluster_id, format=None):
        #try:
        #   return Cluster.objects.get(id=id)
        #except Cluster.DoesNotExist:
        #   raise Http404
        return Response("todo")

    def destroy(self, request, cluster_id, format=None):
        return Response("todo")

    @detail_route(methods=['post'])
    def stop(self, request, cluster_id, format=None):
        return Response("todo")
    
    @detail_route(methods=['post'])
    def start(self, request, cluster_id, format=None):
        return Response("todo")
    
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
    def get_object(self, id):
        # try:
        #    return Project.objects.get(id=id)
        # except Project.DoesNotExist:
        #    raise Http404
        return None

    def get(self, request, id, format=None):
        """
        Retrieve a project instance.
        """
        # project = self.get_object(id)
        # serializer = ProjectSerializer(project)
        # return Response(serializer.data)
        return Response("todo")
    
    def put(self, request, id, format=None):
        """
        Update a project instance.
        """
        # project = self.get_object(id)
        # serializer = ProjectSerializer(project, data=request.data)
        # if serializer.is_valid():
        #    serializer.save()
        #    return Response(serializer.data)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("todo")
        
    def delete(self, request, id, format=None):
        """
        Delete a project instance.
        """
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
        
