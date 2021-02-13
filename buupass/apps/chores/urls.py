from django.urls import path

from .views import ChoresList


urlpatterns = [
    path('chores', ChoresList.as_view(),
         name='chores'),
]
