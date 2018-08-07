"""travel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path

from trvl_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_user/', views.AddUserView.as_view(), name='add-user'),
    path('', views.UserLoginView.as_view(), name='login'),
    path('accounts/login/', views.UserLoginView.as_view(), name='login'),
    path('logout', views.UserLogoutView.as_view(), name='logout'),
    path('index/', views.IndexView.as_view(), name='index'),
    path('add_travel/', views.TravelCreateView.as_view(), name='add-travel'),
    path('list_travel/', views.TravelListView.as_view(), name='list-travel'),
    path('detail_travel/<int:pk>/', views.TravelDetailView.as_view(), name='detail-travel'),
    path('delete_travel/<int:pk>/', views.TravelDeleteView.as_view(), name='delete-travel'),
    path('update_travel/<int:pk>/', views.TravelUpdateView.as_view(), name='update-travel'),

]
