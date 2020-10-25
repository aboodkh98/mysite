
from django.urls import path
from . import views
app_name = "music"
urlpatterns = [
    path('song/', views.SongViwe.as_view(), name='song'),
    path('<int:pk>/', views.DetailViwe.as_view(), name='detail'),
    path('album/add/', views.CreateAlbum.as_view(), name='add-album'),
    path('song/add/', views.CreateSong.as_view(), name='add-song'),
    path('album/update/<int:pk>/', views.UpdateAlbum.as_view(), name='Update-album'),
    path('song/update/<int:pk>/', views.UpdateSong.as_view(), name='Update-song'),
    path('album/<int:pk>/delete/', views.DeleteAlbum.as_view(), name='Delete-album'),
    path('song/<int:pk>/delete/', views.DeleteSong.as_view(), name='Delete-song'),

]
