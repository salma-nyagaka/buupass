from .models import Chores
from .serializers import ChoresSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ChoresList(APIView):
    """
    List all chores, or create a new chore.
    """
    def get(self, request, format=None):
        chores = Chores.objects.all()
        serializer = ChoresSerializer(chores, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ChoresSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChoresDetail(APIView):
    def get_object(self, pk):
        try:
            return Chores.objects.get(pk=pk)
        except Chores.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        chore = self.get_object(pk)
        serializer = ChoresSerializer(chore, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk, format=None):
        chore = self.get_object(pk)
        serializer = ChoresSerializer(chore)
        return Response(serializer.data)