from django.urls import path
from .views import user

app_name = "acsys"

urlpatterns = [
    path('user/', user.index, name='index'),
    path('user/login', user.login, name='login'),
    path('user/signup', user.signup, name='signup'),
    # path('calorie/save_calorie', views.calorie, name='save_calorie'),
]