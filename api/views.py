#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ipware import get_client_ip
import requests
import os

# Create your views here.
class HelloView(APIView):
    def get(self, request):
        visitor_name = request.query_params.get('visitor_name', 'Guest')
        client_ip, is_routable = get_client_ip(request)
        
        if client_ip is None:
            client_ip = "127.0.0.1"  # Default IP if not found

        
           
        location = "Osun"  
        api_key = os.getenv('WEATHER_API_KEY')
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
        weather_response = requests.get(weather_url)
        weather_data = weather_response.json()
        temperature = weather_data['main']['temp']

        greeting = f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {location}"

        data = {
            "client_ip": client_ip,
            "location": location,
            "greeting": greeting
        }

        return Response(data, status=status.HTTP_200_OK)