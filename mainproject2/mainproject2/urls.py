"""mainproject2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('hr/', views.HR),
    path('emptable/',views.emptable),
    path('viewemp/',views.viewemp),
    path('empform/', views.empform_view),
    path('delete/<int:id>', views.delete_view),
    path('update/<int:id>',views.update_view),
    path('newsform/', views.newsform_view),
    path('mainnews/',views.mainnews_view),
    path('employee/',views.employee),
    path('viewnews/',views.viewnews),
    path('calform/', views.calendarform_view),
    path('viewcal/',views.viewcalendar),
    path('vct/',views.caltable),
    path('accounts/',include('django.contrib.auth.urls')),
    path('logout/',views.logout),
    path('signup/',views.signup),
]
