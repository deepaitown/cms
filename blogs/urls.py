from django.conf.urls import url
from blogs import views as blog_views

urlpatterns = [
    url(r'^create/', blog_views.createblog, name='createblog'),
    
]