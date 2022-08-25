from django.urls import path
from .views import home,get_category

urlpatterns=[

	path('',home,name='home'),
	path('category/<int:category_id>/', get_category, name='category'),

]