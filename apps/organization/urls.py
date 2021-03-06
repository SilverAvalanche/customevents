from django.conf.urls import patterns, url, include
from apps.organization import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'organizations', views.OrganizationViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

)
