from rest_framework import viewsets
from .serializers import PersonSerializer
from .models import Person

# Create your views here.
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer