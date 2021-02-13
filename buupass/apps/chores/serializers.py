from rest_framework import serializers
from .models import Chores


class ChoresSerializer(serializers.ModelSerializer):
    """class for serializing the chores"""

    class Meta:
        model = Chores 
        field = ['id', 'title', 'summary', 'completed', 'date_completed']

