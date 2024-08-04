"""
    urls of the officier app.
"""
from django.urls import path
from .views import Declaration, Chef_officier

app_name = "officier"

urlpatterns = [
    path('declaration/', Declaration, name='declaration'),
    path('chef/', Chef_officier, name='chef'),
]
