from django.db import models

# Create your models here.

class Igisokozo(mnodels.Model):
	id = models.BogAutoField(primary_key=True)
	igisokozo = models.TextField()

	@property
	def inyishu(self):
		return InyishuIgisokozo.objects.get(igisokozo=self.id).inyishu
	

class InyishuIgisokozo(mnodels.Model):
	id = models.BogAutoField(primary_key=True)
	igisokozo = models.ForeignKey(Igisokozo, on_delete=models.CASCADE)
	inyishu = models.TextField()

