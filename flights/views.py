from datetime import datetime

from rest_framework.generics import ListAPIView

from .models import Booking, Flight
from .serializers import BookingSerializer, FlightSerializer


class FlightsList(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class BookingsList(ListAPIView):
    queryset = Booking.objects.filter(date__gte=datetime.today())
    serializer_class = BookingSerializer
