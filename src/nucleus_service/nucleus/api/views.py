from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# @api_view(['GET'])
# def cluster_list(request):
#    return Response("response")

class Cluster(APIView):
    """
    List all clusters, or create a new cluster.
    """
    def get(self, request, format=None):
        #clusters = Cluster.objects.all()
        #serializer = CLusterSerializer(clusters, many=True)
        #return Response(serializer.data)
        return Response("todo")
        
    def post(self, request, format=None):
        #serializer = ClusterSerializer(data=request.data)
        #if serializer.is_valid():
        #    serializer.save()
        #    return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("todo")
