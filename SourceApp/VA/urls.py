from django.contrib import admin
from django.urls import path
from VA.views import login, tabnabbing

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login.index, name='index'),
    path('va/login/', login.loginPageDisplay, name='login'),
    path('va/home/', login.homePageDisplay, name='home'),
    path('va/logout/', login.logoutPage, name='logout'),
    path('va/tabnabbing/', tabnabbing.tabnabbingPage, name='tabnabbing'),
    path('va/tabnabbing-fixed/', tabnabbing.tabnabbingFixedPage, name='tabnabbing-fixed')
]
