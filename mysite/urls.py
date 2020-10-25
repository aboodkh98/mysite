
from django.contrib import admin
from django.urls import path,include
from music import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('music/', include('music.urls')),
    path('', views.IndexViwe.as_view() , name='index'),
]
if settings.DEBUG :
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)