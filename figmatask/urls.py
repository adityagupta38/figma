"""figmatask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from figma import views
from django.conf.urls.static import static
from figmatask import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('userregisteration', views.user_registeration, name='user_registeration'),
    path('userprofile<int:pk>', views.user_profile, name='user_profile'),
    path('adduserprofile<int:pk>', views.add_user_profile, name='add_user_profile'),
    path('profileupdate<int:pk>', views.update_user_profile, name='profile_update'),
    path('uploadpost<int:pk>', views.post_upload, name='upload_post'),
    path('logout', views.logout, name='logout'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
