from datetime import datetime
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


from buupass.helpers.endpoint_response import \
    get_success_responses
from .models import Chores
from buupass.apps.authentication.models import \
    User
from .serializers import ChoresSerializer


class ChoresList(APIView):
    permission_classes = (IsAuthenticated,)

    """List all chores"""

    def get(self, request, format=None):
        chores = Chores.objects.all()
        serializer = ChoresSerializer(chores, many=True)
        return get_success_responses(
            data=serializer.data,
            message="Successfully fetched all the chores",
            status_code=status.HTTP_201_CREATED
        )

    """Create new chores"""

    def post(self, request, format=None):
        try:
            user_id = request.user.id
            user = User.objects.get(id=user_id)

            if (user.type == "OWNER"):
                serializer = ChoresSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return get_success_responses(
                        data=serializer.data,
                        message="Successfully created a chore",
                        status_code=status.HTTP_201_CREATED
                    )
                return get_success_responses(
                    data=serializer.errors,
                    message="Error Message",
                    status_code=status.HTTP_400_BAD_REQUEST
                )
            return Response("You are not allowed to perform this action")
        except Exception as e:
            return Response({"Error message": "{}".format(e)})


class ChoresDetail(APIView):
    """Get a specific chore"""
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Chores.objects.get(pk=pk)
        except Chores.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        chore = self.get_object(pk)
        try:
            user_id = request.user.id
            user = User.objects.get(id=user_id)

            if (user.type == "OWNER"):
                serializer = ChoresSerializer(chore, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return get_success_responses(
                        data=serializer.data,
                        message="Successfully updated the chore",
                        status_code=status.HTTP_200_OK
                    )
                return get_success_responses(
                    data=serializer.errors,
                    message="Error Message",
                    status_code=status.HTTP_400_BAD_REQUEST
                )
            return Response("You are not allowed to perform this action")
        except Exception as e:
            return Response({"Error message": "{}".format(e)})

    def get(self, request, pk, format=None):
        chore = self.get_object(pk)
        serializer = ChoresSerializer(chore)
        return get_success_responses(
            data=serializer.data,
            message="Successfully fetched the chore",
            status_code=status.HTTP_200_OK
        )

    def delete(self, request, pk, format=None):
        chore = self.get_object(pk)
        try:
            user_id = request.user.id
            user = User.objects.get(id=user_id)

            if (user.type == "OWNER"):
                chore.delete()
                return Response({"Success: successfully deleted the chore"}, status=status.HTTP_200_OK)
            return Response("You are not allowed to perform this action")
        except Exception as e:
            return Response({"Error message": "{}".format(e)})


class ChoreUpdate(APIView):
    """Update status of the chore"""

    def put(self, request, pk, format=None):
        chore = Chores.objects.get(id=pk)
        serializer = ChoresSerializer(chore, data=request.data)
        chore.completed = True
        chore.save()

        return Response(
            "Chore completed successfully"
        )
