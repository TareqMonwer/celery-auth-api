from django.urls import path
from core.views import list_urls


app_name='core'
urlpatterns = [
    path('', list_urls, name='list_urls'),
]
