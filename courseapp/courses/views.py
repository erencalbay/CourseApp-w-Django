from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

data = {
    "programlama" : "programlama kategorisine ait kurslar",
    "web-gelistirme" : "web geliştirme kategorisine ait kurslar kategorisine ait kurslar",
    "mobil" : "mobil kategorisine ait kurslar",
}

def kurslar(request):
    return HttpResponse('kurs listesi')

def details(request, kurs_adi):
    return HttpResponse(f'{kurs_adi} detay sayfasi')

def getCoursesByCategory(request, category_name):

    try:
        category_text = data[category_name]
        return HttpResponse(category_text)
    except:
        return HttpResponseNotFound("yanlis kategori secimi")


def getCoursesByCategoryId(request, category_id):
    category_list = list(data.keys())
    if(category_id > len(category_list)):
        return HttpResponseNotFound("NASIL YANİ kategori secimi")        
    category_name = category_list[category_id - 1]

    redirect_url = reverse('courses_by_category', args=[category_name])

    return redirect(redirect_url)