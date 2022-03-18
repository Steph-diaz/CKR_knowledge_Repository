from django.urls import include, path
from rest_framework import routers
from ckr_knowledge_repository.api.views import EntryViewSet

router = routers.DefaultRouter()
router.register(r'entry', EntryViewSet)
# router.register(r'experiment_images', views.ExperimentImageViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
