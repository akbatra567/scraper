from scrapy_djangoitem import DjangoItem
from myapi.models import Job


class JobItem(DjangoItem):
    django_model = Job