from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings
#from views import category, project# search



urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('index/', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('category/', views.category, name="category"),
    path('search/', views.search, name="search"),
    path('Project/', views.my_project, name="my_project"),
    path('faq/', views.faq, name="faq"),
    #path('slug/', views.slug, name="slug"),
    

    
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)