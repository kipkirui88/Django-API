from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import StudentSerializer, ParentSerializer
from .models import Student, Parent

# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class ParentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer