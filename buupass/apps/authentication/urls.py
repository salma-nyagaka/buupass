from django.urls import path
from .views import RegistrationAPIView, LoginAPIView

app_name = "authentication"

urlpatterns = [
    path('signup', RegistrationAPIView.as_view(),
         name='manager'),
    path('signin', LoginAPIView.as_view(),
         name='user_login'),
]
