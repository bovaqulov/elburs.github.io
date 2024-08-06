from django.db import models


class AboutUs(models.Model):
	title = models.CharField(max_length=200, verbose_name="Biz haqimizda")
	text = models.TextField(default="Uzoq yillik tajrba")
	image = models.ImageField(upload_to="about_us_image/")
	is_published = models.BooleanField(default=False)

	def __str__(self):
		return self.title