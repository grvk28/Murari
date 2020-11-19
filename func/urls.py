from django.conf.urls import patterns, url, include
from func import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^products',views.products,name='products'),
                       url(r'^brands',views.brands,name='brands'),
                       url(r'^about',views.about,name='about'),
                       url(r'^login',views.login,name='login'),
                       url(r'^order',views.order,name='order'),
                       url(r'^home',views.home,name='home'),
                       )