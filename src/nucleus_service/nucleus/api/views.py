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

class ComputeViewSet(ModelViewSet):
    lookup_field = 'compute_id'
    serializer_class = ComputeSerializer

    def list(self, request, compute_id_cluster_id, format=None):
        return Response("todo")

    def retrieve(self, request, compute_id, compute_id_cluster_id, format=None):
        return Response("todo")

    def destroy(self, request, compute_id, compute_id_cluster_id, format=None):
        return Response("todo")
    
class StorageViewSet(ModelViewSet):
    lookup_field = 'storage_id'
    serializer_class = StorageSerializer

    def list(self, request, compute_id_cluster_id, storage_id_compute_id, format=None):
        return Response("todo")

    def retrieve(self, request, storage_id, compute_id_cluster_id, storage_id_compute_id, format=None):
        return Response("todo")

    def destroy(self, request, storage_id, compute_id_cluster_id, storage_id_compute_id, format=None):
        return Response("todo")
   
class UserViewSet(ModelViewSet):
    lookup_field = 'user_id'
    serializer_class = UserSerializer

    def list(self, request, format=None):
        """
        List all Persons that can create clusters.
        We will investigate djangos build in classes for that.
        """
        return Response("todo")

    def retrieve(self, request, user_id, format=None):
        return Response("todo")

    def destroy(self, request, user_id, format=None):
        return Response("todo")

class ProjectViewSet(ModelViewSet):
    lookup_field = 'project_id'
    serializer_class = ProjectSerializer

    def list(self, request, format=None):
        """
        List all Projects that can create clusters.
        We will investigate if django has already a project as part of user management.
        """
        return Response("todo")

    def retrieve(self, request, project_id, format=None):
        return Response("todo")

    def destroy(self, request, project_id, format=None):
        return Response("todo")
