from django.urls import path
from portfolioapp import views

urlpatterns = [
    path('', views.portfolio, name='portfolio')
]
