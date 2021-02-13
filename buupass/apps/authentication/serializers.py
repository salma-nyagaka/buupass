from django.contrib.auth import authenticate

from rest_framework import serializers, validators
from rest_framework.validators import UniqueValidator

from buupass.apps.authentication.backends import \
    JWTAuthentication
from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    """Serializers registration requests and creates a new user."""

    def __init__(self, *args, **kwargs):
        super(RegistrationSerializer, self).__init__(*args, **kwargs)

        # Override the default error_messages with a custom field error
        for field in self.fields:
            error_messages = self.fields[field].error_messages
            error_messages['null'] = error_messages['blank'] \
                = error_messages['required'] \
                = 'Please fill in the {}.'.format(field)

    # email = serializers.RegexField(
    #     regex="^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$",
    #     validators=[
    #         validators.UniqueValidator(
    #             queryset=User.objects.all(),
    #             message='Email address already exists',
    #         )
    #     ],
    # )

    # Ensure that username is unique, does not exist,
    #  cannot be left be blank, has a minimum of 5 characters
    # has alphanumerics only
    username = serializers.RegexField(
        regex='^[A-Za-z ]+\d*$',
        min_length=4,
        max_length=30,
        required=True,
        validators=[UniqueValidator(
            queryset=User.objects.all(),
            message='The username already exists. Kindly try another.'
        )],
        error_messages={
            'min_length': 'Username must have a minimum of 4 characters.',
            'max_length': 'Username must have a maximum of 30 characters.',
            'invalid': 'Username can only have alphabet characters.'
        }
    )

    # Ensure passwords are at least 8 characters long,
    # at least one letter and at least one number
    password = serializers.RegexField(
        regex='^[A-Za-z0-9 ]+\d*$',
        min_length=4,
        max_length=30,
        write_only=True,
        required=True,
        error_messages={
            'max_length': 'Password cannot be more than 128 characters',
            'min_length': 'Password must have at least 7 characters',
            'invalid': 'Invalid password',
        }
    )
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        # List all of the fields that could possibly be included in a request
        # or response, including fields specified explicitly above.
        fields = ['email', 'username', 'password', 'token']

    def create(self, validated_data):
        # Use the `create_user` method we wrote earlier to create a new user.
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    """The class to serialize login details"""
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        """
        The `validate` method is where we make sure that the current
        instance of `LoginSerializer` has "valid". In the case of logging a
        user in, this means validating that they've provided an email
        and password and that this combination matches one of the users in
        our database.
        """
        email = data.get('email', None)
        password = data.get('password', None)

        # As mentioned above, an email is required. Raise an exception if an
        # email is not provided.
        if email is None:
            raise serializers.ValidationError(
                'Your email address is required to log in.'
            )

        # As mentioned above, a password is required. Raise an exception if a
        # password is not provided.
        if not password:
            raise serializers.ValidationError(
                'Kindly enter your password to log in.'
            )

        # The `authenticate` method is provided by Django and handles checking
        # for a user that matches this email/password combination. Notice how
        # we pass `email` as the `username` value. Remember that, in our User
        # model, we set `USERNAME_FIELD` as `username`.
        user = authenticate(email=email, password=password)

        # `authenticate` will return `None`. Raise an exception in this case.
        if user is None:
            raise serializers.ValidationError(
                'Either your email or password isn’t right'
            )

        # Django provides a flag on our `User` model called `is_active`. The
        # purpose of this flag to tell us whether the user has been banned
        # or otherwise deactivated. This will almost never be the case, but
        # it is worth checking for. Raise an exception in this case.
        # if not user.is_active:
        #     raise serializers.ValidationError(
        #         'Your account is inactive. Kindly check your email for an '
        #         'activation link to activate '
        #     )
        token = JWTAuthentication.generate_token(email)

        """
        The `validate` method should return a dictionary of validated data.
        This is the data that is passed to the `create` and `update` methods
        that we will see later on.
        """
        return {
            'email': user.email,
            'username': user.username,
            'token': token
        }
