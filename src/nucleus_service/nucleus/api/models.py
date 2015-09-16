from django.db import models

"""
class User(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.CharField(max_length=24)
    email = models.CharField(max_length=100)            

    class Meta:
        ordering = ('name',)
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('username', 'firstname', 'lastname', 'email', 'created')
        
class Project(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('name')
                
class Cluster(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)

class ClusterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('name')
        
                
class Storagepool(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)
        
class StoragepoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('name')
"""
