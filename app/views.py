from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import string
import random
from .models import Url
from .serializers import UrlSerializer

@method_decorator(csrf_exempt, name='dispatch')
class IndexView(APIView):
    def get(self, request):
        return render(request, "app/index.html")
    
@method_decorator(csrf_exempt, name='dispatch')
class UrlShortener(APIView):
    def get(self, request, short_url, *args,  **kwargs):
        try:
            url_obj = Url.objects.get(short_url=short_url)
        except Url.DoesNotExist:
            return Response({"error": "URL doesn't exist"}, status=status.HTTP_404_NOT_FOUND)
        
        url_obj.clicks += 1
        url_obj.save()
        return redirect(url_obj.long_url)
        
    def post(self, request, *args, **kwargs):
        data = request.data
        ser_obj = UrlSerializer(data=data)
        
        if ser_obj.is_valid():
            long_url = ser_obj.validated_data["long_url"]
        else:
            return Response({"error": "Invalid URL"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Check if the long_url already exists in the database
        obj = Url.objects.filter(long_url=long_url).first()
        if obj:
            # If it exists, serialize and return the existing object
            response_data = UrlSerializer(obj).data
            response_data['short_url'] = f"{request.get_host()}/{response_data['short_url']}"
            return Response(response_data, status=status.HTTP_200_OK)
        
        # If not found, create a new short URL
        created = False
        count = 0
        while not created and count <= 20:    
            short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
            obj, created = Url.objects.get_or_create(long_url=long_url, defaults={'short_url': short_url})
            count += 1
        
        if not created:
            return Response({"error": "Failed to create a unique short URL"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        response_data = UrlSerializer(obj).data
        response_data['short_url'] = f"{request.get_host()}/{response_data['short_url']}"
        
        return Response(response_data, status=status.HTTP_201_CREATED)

