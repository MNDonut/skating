from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Event
from .serializers import EvenSerializer


class EventsView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EvenSerializer
