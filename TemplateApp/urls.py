from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    # path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('members', views.members, name='members'),
    path('member/<int:id>', views.member, name='member'),
    # path('hello', views.index, name='index'),
    # path('page/<str:user_name>', views.user_page, name='user_page'),
    # path('num_page/<int:number>', views.number_page, name='number_page'),
    # path('num_page/<str:user_name>/<int:number>', views.number_page, name='number_page'),
]