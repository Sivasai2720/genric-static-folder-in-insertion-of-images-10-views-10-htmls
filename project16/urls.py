"""
URL configuration for project16 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('sy1/',sy1,name='sy1'),
    path('sy2/',sy2,name='sy2'),
    path('sy3/',sy3,name='sy3'),
    path('sy4/',sy4,name='sy4'),
    path('sy5/',sy5,name='sy5'),
    path('sy6/',sy6,name='sy6'),
    path('sy7/',sy7,name='sy7'),
    path('sy8/',sy8,name='sy8'),
    path('sy9/',sy9,name='sy9'),
    path('sy10/',sy10,name='sy10'),
]
