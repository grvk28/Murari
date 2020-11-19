"""gkm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from func import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^func/', include('func.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^products',views.products,name='products'),
    url(r'^brands',views.brands,name='brands'),
    url(r'^about',views.about,name='about'),
    url(r'^login',views.login,name='login'),
    url(r'^order',views.order,name='order'),
    url(r'^home',views.home,name='home'),
]
