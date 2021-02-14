from django.urls import path

from .views import ChoresList, ChoresDetail, ChoreUpdate


urlpatterns = [
    path('chores', ChoresList.as_view(),
         name='chores'),
    path('chores/<str:pk>/', ChoresDetail.as_view()),
    path('chores/status/<str:pk>/', ChoreUpdate.as_view()),
]
