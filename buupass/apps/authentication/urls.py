from django.urls import path
from .views import OwnerRegistratiomAPIView, LoginAPIView 

app_name = "authentication"

urlpatterns = [
    path('signup/owner', OwnerRegistratiomAPIView.as_view(),
         name='owner'),
#     path('signup/owner', RegistrationAPIView.as_view(),
#          name='owner'),
    path('signin', LoginAPIView.as_view(),
         name='user_login'),
]
