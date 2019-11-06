from django.urls import path
from BasicApp.views import index, other, relative, base, register, user_login

# TEMPLATE TAGGING

app_name = 'basic_app'


urlpatterns =[
    path('relative/', relative, name='relative'),
    path('other/', other, name='other'),
    path('base/', base, name='base'),
    path('index/', index, name='index'),
    path('register/', register, name='register'),
    path('user_login/', user_login, name='user_login')
]
