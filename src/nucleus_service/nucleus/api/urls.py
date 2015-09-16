from django.conf.urls import patterns, url
import views

urlpatterns = patterns(
    'api.views',
    url(r'^cluster$', 'cluster_list', name='cluster_list'),
    url(r'^cluster/(?P<cluster_name>\w+)/stop$', 'cluster_stop', name='cluster_stop'),
    url(r'^cluster/(?P<cluster_name>\w+)/start$', 'cluster_start', name='cluster_start'),
    url(r'^/gregor/clusters/$', views.ClusterList.as_view()),
    url(r'^/users/$', views.UserList.as_view()),
    url(r'^/projects/$', views.ProjectList.as_view()),    
)
