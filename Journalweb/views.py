from django.shortcuts import render
from django.db.models.fields.related import ForeignKey
from django.shortcuts import render,HttpResponse
from django.shortcuts import render,HttpResponse
#from django.shortcuts import render,get_objects_or_404
from django.template import loader
from django.db.models import Q
#from example.config import Pagination
from .models import Category,projects

# Create your views here.

def about(request):
    return render(request,"About.html")


def index(request):
    return render(request,"Index.html")


def contact(request):
    return render(request,"Contact.html")


def category(request,):
    #THIS IS NOT CHANGED YET
    All_Category = Category.objects.all()
    return render(request,'Category.html', {'All_Category': All_Category})

def search(request):
    tempelate = 'journal/PROJECT.HTML'
    query =request.GET.get('q')
    result = project.objects.filter(Q(tittle__icontains=query)| Q(body__icontains=query)) 
    pages = Pagination(request, result, num=1)

    contex = {
        'Items': pages[0],
        'page_range': pages[1],
    }

    return render(request,tempelat,contex)


def my_project(request, slug):
    project = get_objects_or_404(project, slug=slug)
    objects_list = project.objects.filter(status='publish')
    pages = Pagination(request, objects_list, 1)

    # all_projects = {
    #     'Items':pages = [0],
    #     'page_range': pages = [1],
    #  }
    #THIS HAS NOT BEEN CHANGED YET
    all_projects = projects.objects.all()
    return render(request, 'Journalweb/PROJECT.HTML', {'all_projects': all_projects})

    

    


def faq(request):
    return render(request,"Faq.html")



