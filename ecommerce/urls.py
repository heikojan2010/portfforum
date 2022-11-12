from django.conf import settings
from django.conf.urls.static import static 
from django.contrib import admin
from django.urls import include, path, re_path, reverse
from rest_framework import routers


# Routers,,, to provide automatically determined URL conf...
router = routers.DefaultRouter()


urlpatterns = [
    #path('admin/defender/', include('defender.urls')), # DEFENDER admin link,,
    path('admin/', admin.site.urls), # normal admin

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("__reload__/", include("django_browser_reload.urls")),
    #path('', include('chatforum.urls')), # STYLE,,,
    
    path('', include('theme.urls')), # STYLE,,,

   
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
