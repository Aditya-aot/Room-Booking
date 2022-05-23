from django.urls import path
from . import views
# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib.auth.models import  User

urlpatterns = [
    path('', views.book_view , name='book_view') ,
    path('home', views.home_view , name='home_view') ,
    path('done', views.done_view , name='done_view') ,
 
 
]

