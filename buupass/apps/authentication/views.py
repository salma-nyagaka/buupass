import os
import jwt
import datetime
from django.conf import settings
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
# from mpesa.apps.api.models.


from buupass.apps.authentication.backends import \
    JWTAuthentication
from buupass.helpers.endpoint_response import \
    get_success_responses
from .models import User
from .renderers import UserJSONRenderer
from .serializers import LoginSerializer, RegistrationSerializer


class RegistrationAPIView(GenericAPIView):
    """Register a new user"""
    # Allow any user (authenticated or not) to hit this endpoint.
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = RegistrationSerializer

    def post(self, request, **kwargs):
        """ Signup a new user """
        email, username, password = request.data.get(
            'email', None), request.data.get(
            'username', None), request.data.get('password', None)

        user = {"email": email, "username": username, "password": password}

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        response_data = {
            "username": username,
            "email": email
        }

        return get_success_responses(
            data=response_data,
            message="Successfully created an account with link pay as {}".format(username),
            status_code=status.HTTP_201_CREATED
        )

    def get(self, request):
        return Response(
            data={
                "message": 'Only POST requests are allowed to this endpoint.'
            })



class LoginAPIView(GenericAPIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request):
        """Login a user"""
        email, password = request.data.get('email', None), request.data.get(
            'password', None)

        # import pdb
        # pdb.set_trace()

        user = {"email": email, "password": password}
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        user_data = serializer.data

        user = User.get_user(user_data['email'])
        userdata = {
            "id": user.id,
            "email": user.email,
            "username": user.username
        }
        user_data['token'] = \
            JWTAuthentication.generate_token(userdata=userdata)

        return get_success_responses(
            data=user_data,
            message="You have successfully logged in",
            status_code=status.HTTP_200_OK
        )

    def get(self):
        """Get a user"""
        return Response(
            data={
                "message": 'Only post requests are allowed to this endpoint.'
            })

