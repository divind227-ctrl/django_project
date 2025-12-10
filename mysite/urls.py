from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),

    path('dashboard/', include('dashboard.urls')),

    # redirect home to dashboard
    path('', lambda request: redirect('/dashboard/')),
]
