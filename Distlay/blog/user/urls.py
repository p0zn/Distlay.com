from django.contrib import admin
from django.urls import path , reverse_lazy
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = "user"


urlpatterns = [
    path('register/',views.register,name="register"),
    path('login/',views.loginUser,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('profile/',views.profileUser,name="profile"),
    
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)