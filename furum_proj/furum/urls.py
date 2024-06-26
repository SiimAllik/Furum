"""
URL configuration for furum_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from furumapp.models import Post, Comment, Topic
from furumapp.views import Home_View

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Topic)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('furum/', include('furumapp.urls')),
    path('', Home_View),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

