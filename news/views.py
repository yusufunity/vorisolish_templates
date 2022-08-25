from django.shortcuts import render
from .models import News,Category



def home(request):
	news=News.objects.all()
	catego_obj=Category.objects.all()
	context={
		'news':news,
		'catego_obj':catego_obj,
		
		'title':"Yusufdev blogi"

	}
	return render(request, template_name='index.html',context=context)


def get_category(request, category_id):
	
	news = News.objects.filter(category_id=category_id)
	
	categories = Category.objects.all()

	category = Category.objects.get(pk=category_id)
	

	context={

		'news':news,
		'categories':categories,
		'category':category

	}	

	return render(request,template_name='category.html',context=context)
