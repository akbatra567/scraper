from rest_framework import viewsets
from .serializers import JobSerializer
from .models import Job


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all().order_by('date_posted')
    serializer_class = JobSerializer