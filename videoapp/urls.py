"""
URL configuration for videoapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from main.views import home,login_view,signup_view,logout_view, add_rating, add_comment, custom_logout_view
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),
    path('signup/', signup_view, name='signup'),

    path('home/', home, name='home'),
    path('add_rating/', home, name='add_rating'),
    path('add_comment/', add_comment, name='add_comment'),
    path('logout/', custom_logout_view, name='logout'),




]