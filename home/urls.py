from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name ='Home'),
    path('<int:question_id>/Menu/', Menu, name ='main')

]