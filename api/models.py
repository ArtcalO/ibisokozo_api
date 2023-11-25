from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.utils.translation import gettext_lazy as _



# Create your models here.




class CustomUser(AbstractUser):
    profile_photo = models.ImageField(max_length=500, blank=True)
    score = models.IntegerField(default=0)
    


 

class Igisokozo(models.Model):
	id = models.BigAutoField(primary_key=True)
	igisokozo = models.TextField()
	itariki = models.DateTimeField(auto_now=True)

	@property
	def inyishu(self):
		return InyishuIgisokozo.objects.get(igisokozo=self.id).inyishu

class IbisokozoCollected(models.Model):
	id = models.BigAutoField(primary_key=True)
	igisokozo = models.TextField()
	inyishu = models.TextField()
	itariki = models.DateTimeField(auto_now=True)


class InyishuIgisokozo(models.Model):
	id = models.BigAutoField(primary_key=True)
	igisokozo = models.ForeignKey(Igisokozo, on_delete=models.CASCADE)
	inyishu = models.TextField()
	insiguro = models.TextField(default="...")
	itariki = models.DateTimeField(auto_now=True)

