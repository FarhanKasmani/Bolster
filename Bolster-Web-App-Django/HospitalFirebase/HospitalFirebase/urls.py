"""HospitalFirebase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from Accounts.views import (patients_view,login_view,dashboard_view,profile_view,verify_view)
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', login_view),
    url(r'^profile', profile_view),
    url(r'^patients/', patients_view),
    url(r'^dashboard/', dashboard_view),
    url(r'^verification/', verify_view),
    #url(r'^profile/', profile_view),

]
