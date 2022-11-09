# theme/urls.py
from django.urls import include, path, re_path, reverse
from django.conf.urls import url
from theme import views




from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('forum/', views.room, name='forum'),
    path('', views.Login, name='login'),
    path('register', views.Register, name="register"),
    path('logout', views.Logout, name="logout"),
    url(r'^(?P<label>[\w-]{,50})/$', views.chat_room, name='chat_room'),
]
