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

