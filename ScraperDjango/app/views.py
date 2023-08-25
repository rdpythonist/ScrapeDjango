from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status,views,response
from .serializers import UrlSerializer,AppDetailsSerializer
from .utils import get_package_names
from .tasks import get_details
from .models import AppDetails

# Create your views here.


def hello(request):
    return HttpResponse("Hello")

## Requested data is playstore url
class APPDetailsAPI(views.APIView):
    serializer_class=UrlSerializer
    def post(self,request):
        #requested_data={"url":"https://play.google.com/store/games?hl=en&gl=US"}
        package_names = get_package_names(request.data["url"])
        get_details.delay(package_names)    
        return response.Response(status=status.HTTP_200_OK)

class AppDataViews(views.APIView):

    def get(self,request):
        """responsed_data= [{
        {
            "id": 239,
            "title": "RAID: Shadow Legends",
            "rating": 1940826,
            "genre": "Role Playing",
            "score": "4.5558"
        },
        {
            "id": 240,
            "title": "Top Eleven Be a Soccer Manager",
            "rating": 6442082,
            "genre": "Sports",
            "score": "4.5625"
        }]"""
        model=AppDetails.objects.all()
        serializer=AppDetailsSerializer(model,many=True)
        return response.Response(serializer.data,status=status.HTTP_200_OK)