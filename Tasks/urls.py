from django.urls import path
from .views import list_crud2
urlpatterns = [
    path('', list_crud2)
]


