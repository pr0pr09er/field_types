from django.contrib import admin
from django.urls import path
from postApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add', views.add_new),
    path('all/', views.show_all),
]

