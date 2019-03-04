from django.db import models
from django.contrib.auth.models import User

class Grievance(models.Model):
    Name = models.CharField(max_length=60)
    title = models.CharField(max_length=255)
    re_date = models.DateTimeField(verbose_name='Complain Date')
    body = models.TextField()
    verifeedback = models.TextField( blank=True, null=True)
    type = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=12)
    status = models.IntegerField(default=0)
    grev_id = models.ForeignKey(User, on_delete=models.CASCADE)
    resolvefeedback = models.TextField( blank=True, null=True)
    position = models.CharField(max_length=10 ,blank=True, null=True)
    verified = models.CharField(max_length=25 ,blank=True, null=True)
    user = models.CharField(max_length=25 ,blank=True, null=True)
    gender = models.CharField(max_length=10 ,blank=True, null=True)
    r_date = models.DateTimeField(blank=True, null=True,verbose_name='Remidial Date')
    v_date = models.DateTimeField(blank=True, null=True,verbose_name='Verified Date')
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.re_date.strftime('%b %e %Y')

    def r_pretty(self):
        return self.r_date.strftime('%b %e %Y')

    def v_pretty(self):
        return self.v_date.strftime('%b %e %Y')
