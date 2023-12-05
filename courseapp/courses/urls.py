from django.http import HttpResponse
from . import views
from django.urls import path


urlpatterns = [ 
    path('', views.kurslar),
    path('list', views.kurslar),
    path('<kurs_adi>', views.details),
    path('kategori/<str:category_name>', views.getCoursesByCategory),
    path('kategori/<int:category_id>', views.getCoursesByCategoryId, name = "courses_by_category")

]