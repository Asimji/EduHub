from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from .models import *
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    if request.method == 'POST':
        # Extract user data from the request
        email = request.data.get('email')
        password = request.data.get('password')
        name = request.data.get('name')
        role = request.data.get('role')

        # Check if username already exists
        if user.objects.filter(email=email).exists():
            return Response({'error': 'Username already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        # Create a new user
        user = CustomUser.objects.create_user(email=email, password=password, name=name, role=role)

        # Generate a token for the user
        # You can use djangorestframework-simplejwt here

        # Log the user in
        login(request, user)
        return Response({'message': 'Registration successful.'}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    if request.method == 'POST':
        # Extract user data from the request
        email = request.data.get('email')
        password = request.data.get('password')

        # Authenticate the user
        user = authenticate(request, username=email, password=password)

        if user is not None:
            # Log the user in
            login(request, user)

            # Generate a token for the user
            # You can use djangorestframework-simplejwt here

            return Response({'message': 'Login successful.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@login_required
def logout_view(request):
    if request.method == 'POST':
        # Log the user out
        logout(request)
        return Response({'message': 'Logout successful.'}, status=status.HTTP_200_OK)
