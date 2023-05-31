from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import RegisterView, MeView, SessionsView, GraphView


urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('<int:pk>/', MeView.as_view(), name='me'),
    path('<int:pk>/session/', SessionsView.as_view(), name='sessions'),
    path('<int:pk>/graph/', GraphView.as_view(), name='graph'),
]
