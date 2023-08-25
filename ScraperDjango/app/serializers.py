from rest_framework import serializers
from .utils import get_package_names
from .tasks import get_details
from .models import AppDetails


class UrlSerializer(serializers.Serializer):
    url=serializers.URLField()

    
class AppDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model=AppDetails
        fields="__all__"
