from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=190)
    salary = models.FloatField(null=True)
    company = models.CharField(null=True, max_length= 190)
    date_posted = models.DateField(null=True)
    last_date = models.DateField(null=True)

    def __str__(self):
        return self.title
