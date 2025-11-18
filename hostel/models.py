from django.db import models

# Create your models here.

class HostelPersonDetails(models.Model):
    name=models.CharField(max_length=20)
    contact=models.BigIntegerField()
    father_name=models.CharField(max_length=20)
    aadhar=models.BigIntegerField()
    address=models.TextField(max_length=50)
    photo=models.ImageField(upload_to='static/images')
    room_no=models.IntegerField()
    date_of_joining=models.DateField()

    def __str__(self):
        return self.name

class HostelFeeDetails(models.Model):
    sharing=models.CharField(max_length=10)
    fee=models.FloatField()

    def __str__(self):
        return f'{self.sharing}-{self.fee}'

class HostelMenu(models.Model):
    day=models.CharField(max_length=10,default='monday')
    breakfast=models.CharField(max_length=30)
    lunch=models.CharField(max_length=50)
    dinner=models.CharField(max_length=50)

    def __str__(Self):
        return f'{self.day} | {self.breakfast} - {self.lunch} - {self.dinner}'