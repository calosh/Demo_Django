"""Demo_Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.conf import settings # new
from django.conf.urls.static import static # new

from app import views

from demo_vue.views import index_vue, get_products

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('demo_ajax.urls')),
    path('', include('demo_leafletjs.urls')),

    path('', include('social_django.urls', namespace='social')),

    path('login/', views.login_facebook),
    path('logout/', views.logout_view, name="logout"),
    
    path('', views.home),
    path("vue/index_vue", index_vue),
    path("vue/get_products", get_products),
]
if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

