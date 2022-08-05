from rest_framework import serializers
from .models import guide, page, section
class guideSerializer(serializers.ModelSerializer):    
    name=serializers.CharField(max_length=255)
    description=serializers.CharField(max_length=255)
    class Meta:
        model=guide
        fields=('__all__')
class pageSerializer(serializers.ModelSerializer):
    name=serializers.CharField(max_length=255)
    description=serializers.CharField(max_length=255)
    guidename=serializers.CharField(max_length=255)
    class Meta:
        model=page
        fields=('__all__')
class sectionSerializer(serializers.ModelSerializer):
    name=serializers.CharField(max_length=255)
    description=serializers.CharField(max_length=255)
    guidename=serializers.CharField(max_length=255)
    pagename=serializers.CharField(max_length=255)
    class Meta:
        model=section
        fields=('__all__')
