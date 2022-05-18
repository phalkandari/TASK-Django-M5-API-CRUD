from datetime import datetime

from rest_framework.generics import ListAPIView

from .models import Booking, Flight
from .serializers import BookingListSerializer, FlightListSerializer


class FlightListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightListSerializer


class BookingListView(ListAPIView):
    queryset = Booking.objects.filter(date__gte=datetime.today())
    serializer_class = BookingListSerializer
