
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import jwt
from django.conf import settings

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    email = request.data.get('email')
    password = request.data.get('password')
    name = request.data.get('name')  # Corrected variable name
    role = request.data.get('role')

    if len(password) > 5:
        if not User.objects.filter(email=email).exists():
            user = User.objects.create_user(username=email, email=email, password=password, role=role, name=name)  # Corrected variable names
            user.save()
            return Response({'msg': f'{name} is Successfully Register'}, status=status.HTTP_200_OK)
        else:
            return Response({'msg': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'msg': 'Password length is below the required level or incorrect email format'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = authenticate(request, username=email, password=password)

    if user:
        token = jwt.encode({'user_id': user.id, 'email': user.email}, settings.SECRET_KEY, algorithm='HS256')
        return Response({'msg': f'Welcome {user.first_name} You are Now Login', 'token': token}, status=status.HTTP_200_OK)
    else:
        return Response({'msg': 'Incorrect Email or Password'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def logout_view(request):
    token = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[1]

    if token:
        # You can implement your own logic to blacklist tokens if needed.
        # For simplicity, we will just log the user out without any additional checks.
        logout(request)
        return Response({'msg': 'Logout Successfully'}, status=status.HTTP_200_OK)
    else:
        return Response({'msg': 'You are not authorized'}, status=status.HTTP_401_UNAUTHORIZED)

        
