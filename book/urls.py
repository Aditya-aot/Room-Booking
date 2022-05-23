from django.urls import path
from . import views
# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib.auth.models import  User

urlpatterns = [
    path('', views.book_view , name='book_view') ,
    path('home', views.home_view , name='home_view') ,
    path('more', views.more_view , name='more_view') ,
    path('boys', views.boys_view , name='boys_view') ,
    path('girls', views.girls_view , name='girls_view') ,
    path('done', views.done_view , name='done_view') ,
 
 
]

