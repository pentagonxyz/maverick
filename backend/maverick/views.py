from rest_framework import status
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import JsonResponse
from maverick.serializers import MyTokenObtainPairSerializer, RegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from models import MaverickUser
from rest_framework.permissions import AllowAny, IsAuthenticated


# Create your views here.

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = MaverickUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

# Test
@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/maverick/login/',
        '/maverick/register/',
        '/maverick/login/refresh/'
    ]
    return Response(routes)

# Example Endpoint
# Requires authentication to access
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def test_endpoint(request):
    if request.method == 'GET':
        data = f"Congratulation {request.user}, your API just responded to GET request"
        return Response({'response': data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = request.POST.get('text')
        data = f'Congratulation your API just responded to POST request with text: {text}'
        return Response({'response': data}, status=status.HTTP_200_OK)
    return Response({}, status.HTTP_400_BAD_REQUEST)
