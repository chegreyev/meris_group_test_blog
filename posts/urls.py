from rest_framework import routers

from posts.views import PostViewSet

router = routers.DefaultRouter()
router.register('', PostViewSet, basename='posts')

urlpatterns = []
urlpatterns += router.urls
