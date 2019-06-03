from django.urls import path

from demo_ajax.views import suma

urlpatterns = [
    path('suma/', suma, name='suma'),
]
