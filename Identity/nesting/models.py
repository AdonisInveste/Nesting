from django.db import models
from django.contrib.auth.models import User
from Identity import settings
import datetime

# Create your models here.

class Identity_unique(models.Model):

    NIS = models.CharField(max_length = 200, primary_key = True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    Timestamp = models.DateTimeField(auto_now = True)

    First_Name = models.CharField(max_length = 80, null = True,  )

    Last_Name = models.CharField(max_length = 80, null = True, )

    Residence = models.CharField(max_length = 80, blank = True )
