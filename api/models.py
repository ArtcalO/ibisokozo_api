from django.db import models

# Create your models here.

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

class LebonCoin(models.Model):
	id = models.BigAutoField(primary_key=True)
	adresse = models.CharField(max_length=50)
	title = models.CharField(max_length=50)
	prix = models.CharField(max_length=50)
	type_habitat = models.CharField(max_length=50)
	surface_habitable = models.CharField(max_length=50)
	nbr_pieces = models.CharField(max_length=50)
	description = models.TextField()

