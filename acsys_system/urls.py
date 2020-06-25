from django.urls import path
from . import views

urlpatterns = [
    path('user/login', views.user, name='login'),
    path('user/signin', views.user, name='signin'),
    path('calorie/save_calorie', views.calorie, name='save_calorie'),
]