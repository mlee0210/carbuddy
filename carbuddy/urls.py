"""carbuddy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from carbuddy import views as views_carbuddy
from listing import views as views_listing
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views_carbuddy.index, name='index'),
    path('admin/', admin.site.urls),
    path('carmodels/',views_carbuddy.testlink2,),
    path('carmodels/details/',views_listing.details, name='car_details'),
    path('carmodels/details2/',views_listing.details2, name='car_details2'),
    #path('carmodels/',include('listing.urls')),
    path('list/', views_listing.CarInstanceListView.as_view(), name='car_list'),
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

