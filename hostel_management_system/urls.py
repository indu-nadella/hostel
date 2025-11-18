"""
URL configuration for hostel_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from hostel.views import home,register,login_view,view_person,view_fee,view_menu,add_person,add_fee,add_menu,edit_person,edit_fee,edit_menu,delete_person,delete_fee,delete_menu
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',register,name='register'),
    path('login/',login_view,name='login'),
    path('home/',home,name='home'),

    path('person/',view_person,name='person'),
    path('fee/',view_fee,name='fee'),
    path('menu/',view_menu,name='menu'),

    path('add_person',add_person,name='add_person'),
    path('add_fee',add_fee,name='add_fee'),
    path('add_menu',add_menu,name='add_menu'),

    path('edit_person/<int:id>',edit_person,name='edit_person'),
    path('edit_fee/<int:id>',edit_fee,name='edit_fee'),
    path('edit_menu/<int:id>',edit_menu,name='edit_menu'),

    path('delete_person/<int:id>',delete_person,name='delete_person'),
    path('delete_fee/<int:id>',delete_fee,name='delete_fee'),
    path('delete_menu/<int:id>',delete_menu,name='delete_menu'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)