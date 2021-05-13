from rest_framework import serializers
from .models import Job

class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job
        fields = ('title', 'salary', 'company', 'date_posted', 'last_date')