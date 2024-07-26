from django.urls import path
from .views import home, login_page, logout_page, register_page

app_name = "user"

urlpatterns = [
    path('home/', home, name='home'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('register/', register_page, name='register'),
]
