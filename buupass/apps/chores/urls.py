from django.urls import path

from .views import ChoresList, ChoresDetail


urlpatterns = [
    path('chores', ChoresList.as_view(),
         name='chores'),
    path('chores/<str:pk>/', ChoresDetail.as_view()),

]
