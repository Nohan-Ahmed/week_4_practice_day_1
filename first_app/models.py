from django.db import models
import datetime
# Create your models here.
class ExampleModel(models.Model):
    # auto_field = models.AutoField(primary_key=True)
    big_auto_field = models.BigAutoField(primary_key=True)
    big_integer_field = models.BigIntegerField()
    binary_field = models.BinaryField()
    boolean_field = models.BooleanField(default=True)
    char_field  = models.CharField(max_length=30,default= 'se')
    date_time_field = models.DateTimeField(default=datetime.datetime.now())
