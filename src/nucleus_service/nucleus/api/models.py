from django.db import models
from rest_framework import serializers




class User(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.CharField(max_length=24)
    email = models.CharField(max_length=100)            

    class Meta:
        ordering = ('firstname',)
        
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

class Compute(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        pass

class ComputeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compute

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

