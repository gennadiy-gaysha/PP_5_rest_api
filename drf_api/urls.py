from django.contrib import admin
from django.urls import path, include
from .views import endpoint_list, logout_route

urlpatterns = [
    path('', endpoint_list),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('dj-rest-auth/logout/', logout_route),

    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),

    path('', include('profiles.urls')),
    path('', include('paintings.urls')),
    path('', include('comments.urls')),
    path('', include('observations.urls')),
    path('', include('followers.urls')),
]
