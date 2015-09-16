from django.conf.urls import patterns, url
import views

urlpatterns = patterns(
    'api.views',
    url(r'^cluster$', 'cluster_list', name='cluster_list'),
    url(r'^cluster/(?P<cluster_name>\w+)/stop$', 'cluster_stop', name='cluster_stop'),
    url(r'^cluster/(?P<cluster_name>\w+)/start$', 'cluster_start', name='cluster_start'),
    #
    # Cluster
    #
    url(r'clusters$', views.ClusterList.as_view()),
    url(r'^clusters/(?P<cluster_name>\w+)/$', views.ClusterDetail.as_view()),    
    #
    # Users
    #
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<username>[0-9]+)/$', views.UserDetail.as_view()),
    #
    # Projects
    #
    url(r'^projects/$', views.ProjectList.as_view()),
    url(r'^projects/(?P<project_name>[0-9]+)/$', views.ProjectDetail.as_view()),
)
