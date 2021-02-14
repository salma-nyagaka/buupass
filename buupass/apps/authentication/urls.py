from django.urls import path
from .views import OwnerRegistrationAPIView, NannyRegistrationAPIView,\
      LoginAPIView

app_name = "authentication"

urlpatterns = [
    path('signup/owner', OwnerRegistrationAPIView.as_view(),
         name='owner'),
    path('signup/nanny', NannyRegistrationAPIView.as_view(),
         name='nanny'),
    path('signin', LoginAPIView.as_view(),
         name='user_login'),
]
