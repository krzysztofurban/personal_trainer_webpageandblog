from django.conf.urls import url
from startpage import views

urlpatterns = [
    url(r'^$', views.start_page, name='start_page'),
]
