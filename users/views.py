from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone

from .models import User, UserSession
from .serializers import UserSerializer


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        phone_number = request.data.get('phone_number')
        city = request.data.get('city')
        password = request.data.get('password')

        if not username or not phone_number or not city or not password:
            return Response({'error': 'All fields are required'}, 400)
        
        if User.objects.filter(username=username).exists():
            return Response({'error': 'This email is already taken'}, 400)

        if User.objects.filter(phone_number=phone_number).exists():
            return Response({'error': 'This phone number is already taken'}, 400)
        
        user = User.objects.create(
            username=username,
            phone_number=phone_number,
            city=city
        )
        user.set_password(password)
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class MeView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class SessionsView(RetrieveUpdateAPIView, CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response({
            'attended': request.user.sessions.filter(date=timezone.now().date()).exists(),
            'number': request.user.sessions.count()
        })

    def post(self, request, *args, **kwargs):
        if request.user.sessions.filter(date=timezone.now().date()).exists():
            return Response({'error': 'You have already attended it today'}, 400)
        
        UserSession.objects.create(user=request.user)
        return self.get(request, *args, **kwargs)


