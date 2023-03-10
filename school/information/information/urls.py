"""information URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include 
from School_Data import views# new
from School_Data.views import  search_img, SearchResultsView,home
from django.conf.urls.static import static 
from django.conf import settings

app_name = "School_Data"   

urlpatterns = [
    #path('index/', views.index, name='index'),
    #url('r^search/', views.checks, name='Payslip'),
       # path('/search/checks/?P=<int:check_id>/' ,views.checks, name='check'),
    
    #path('search/<int:check_id>/' ,views.checks, name='payslip'),
    #path(r'^search/checks/(?P<check_id>[0-9]+)', views.checks, name='item'),
    path('login/<str:check_id>/' ,views.checks, name='item'),
    
    #path('', views.home, name='start'),
    path('', home.as_view(), name='start'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('admin/', admin.site.urls),
    path('register/', views.register_request, name='register'),
    path('login/', views.login_request, name='login'), 
    path('logout/', views.login_request, name='logout'),
 
]+ static(settings.MEDIA_URL, 
            document_root=settings.MEDIA_ROOT)
   

