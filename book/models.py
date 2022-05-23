from pyexpat import model
from django.db import models
from django.conf import settings
from django.contrib.auth.models import  User, auth
from django.contrib.auth import get_user_model

# Create your models here.

class room_book(models.Model) :
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    a101= models.BooleanField('101',default=False)
    a102= models.BooleanField('102',default=False)
    a103= models.BooleanField('103',default=False)
    a104= models.BooleanField('104',default=False)
    a105= models.BooleanField('105',default=False)
    a106= models.BooleanField('106',default=False)
    a107= models.BooleanField('107',default=False)
    a108= models.BooleanField('108',default=False)


# class user_book(models.Model) :
#     # book = models.ForeignKey(room_book,on_delete=models.CASCADE,null=True)
#     book = models.OneToOneField(room_book, on_delete=models.CASCADE)
#     user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

class girl_room_book(models.Model) :
    user = models.OneToOneField(User,on_delete=models.CASCADE,default=0)
    a101= models.BooleanField('101',default=False)
    a102= models.BooleanField('102',default=False)
    a103= models.BooleanField('103',default=False)
    a104= models.BooleanField('104',default=False)
    a105= models.BooleanField('105',default=False)
    a106= models.BooleanField('106',default=False)
    a107= models.BooleanField('107',default=False)
    a108= models.BooleanField('108',default=False)

