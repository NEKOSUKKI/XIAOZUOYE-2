from django.contrib import admin
from django.urls import path
from teachers_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search_by_name/', views.search_by_name, name='search_by_name'),
    path('search_by_department/', views.search_by_department, name='search_by_department'),
    path('search_results/', views.search_results, name='search_results'),
    path('', views.home, name='home'),
]