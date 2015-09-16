from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def cluster_list(request):
    return Response("response")

@api_view(['POST'])
def cluster_start(request, cluster_name):
    return Response("response cluster start")

@api_view(['POST'])
def cluster_stop(request, cluster_name):
    return Response("response cluster stop")
