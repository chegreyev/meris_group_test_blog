from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from .swagger import swagger_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls'))
    # path('swagger/', include(swagger_patterns)),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
