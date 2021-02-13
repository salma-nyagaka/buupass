from django.urls import path
from .views import OwnerRegistratiomAPIView, NannyRegistratiomAPIView, LoginAPIView 

app_name = "authentication"

urlpatterns = [
    path('signup/owner', OwnerRegistratiomAPIView.as_view(),
         name='owner'),
    path('signup/nanny', NannyRegistratiomAPIView.as_view(),
         name='nanny'),
    path('signin', LoginAPIView.as_view(),
         name='user_login'),
]
