from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='dashboard_home'),           # <-- add this
    path('commercial/', views.commercial_data, name='commercial'),
]
