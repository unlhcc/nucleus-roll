from django.db import models
from rest_framework import serializers

import subprocess


class User(models.Model):
    username = models.CharField(max_length=24)
    created = models.DateTimeField(auto_now_add=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)            

    class Meta:
        ordering = ('username',)
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'firstname', 'lastname', 'email', 'created']
        
class Project(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name']

class Storage(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)

class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = ['name']

class Frontend(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    #name = models.CharField(max_length=100)

    class Meta:
        pass

class FrontendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frontend
        #fields = ['name']

class Group(object):
    def __init__(self, cluster_id, group_id):
        self.group_id = group_id

class GroupSerializer(serializers.Serializer):
    group_id = serializers.IntegerField()

class Compute(object):
    def __init__(self, cluster_id, compute_id):
        self.name = compute_id

    def poweron(self):
        out, err = subprocess.Popen(['ssh', 'dimm@comet-fe1', '"date"'], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        return [out, err]
        

class ComputeSerializer(serializers.Serializer):
    pass

class Cluster(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        pass

class ClusterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cluster

class Storagepool(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)
        
class StoragepoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storagepool
        fields = ['name']
