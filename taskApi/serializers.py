from pyexpat import model
from rest_framework import serializers
from .models import Tasks

class taskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'