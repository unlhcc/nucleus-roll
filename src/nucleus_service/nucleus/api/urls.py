from django.conf.urls import patterns, include, url
import views
from rest_framework.routers import SimpleRouter, Route, DynamicDetailRoute

class ClusterRouter(SimpleRouter):
    routes = [
        Route(
            url=r'^{prefix}/$',
            mapping={'get': 'list'},
            name='{basename}-list',
            initkwargs={'suffix': 'List'}
        ),
        Route(
           url=r'^{prefix}/{lookup}/$',
           mapping={'get': 'retrieve',
            'delete': 'destroy'},
           name='{basename}-detail',
           initkwargs={'suffix': 'Detail'}
        ),
        DynamicDetailRoute(
            url=r'^{prefix}/{lookup}/{methodname}$',
            name='{basename}-{methodname}',
            initkwargs={}
        )
    ]

router = ClusterRouter()
router.register(r'^', views.ClusterViewSet, base_name='cluster')

urlpatterns = patterns(
    'api.views',
    url(r'^cluster', include(router.urls)),
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


