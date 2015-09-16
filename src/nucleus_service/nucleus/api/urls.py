from django.conf.urls import patterns, url

urlpatterns = patterns(
    'api.views',
    url(r'^cluster', 'cluster_list', name='cluster_list')
)
