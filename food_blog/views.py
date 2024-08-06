from django.shortcuts import render

from .models import *

def index(requests):
	about = AboutUs.objects.filter(is_published=True).first()

	context = {
		"title": "Elburs",
		"about_main": {
			"about_title": about.title,
			"about_image": about.image.url,
			"about_text": about.text
		}
	}
	return render(requests, "food_blog/index.html", context=context)


