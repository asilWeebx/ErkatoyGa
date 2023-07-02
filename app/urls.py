from django.urls import path
from app.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', about, name='about'),
    path('sevimli/', sevimli, name='sevimli'),
    path('details/<int:pk>/', details, name='details'),
    path('sotibqiz/', sotibqiz, name='sotibqiz'),
    path('register/', registerPage, name='register'),
    path('login/', loginPage, name='login'),
    path('favourite/<int:id>/', favourite, name='favourites')
]
