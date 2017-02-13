from django.conf.urls import include, url
from. import views

urlpatterns = [
        url(r'^$', views.hello, name = 'hello'),
       url(r'^index', views.index, name = "index"),
       #url(r'^index/', include('vedah_app.urls'), name = 'index'),
        url(r'^products', views.products, name= "products"),
]
