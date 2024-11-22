from django.urls import path

from core.views import home, color

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('color/', color, name='color'),
]
