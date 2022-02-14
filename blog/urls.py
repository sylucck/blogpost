from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='blog'),
   path('category/<slug:slug>/', views.blog_category, name="category"),
   path('about', views.about, name="about"),
   path('contact', views.contact, name="contact"),
   path('search', views.searchposts, name="search"),
   path('success', views.contactsuccess, name="contactsuccess"),
   path('author', views.author, name="author"),
   path('<slug:slug>', views.index_details, name = 'blog-detail'),

]