from django.urls import path
from . import views
urlpatterns = [

    path('login.html',views.Login.as_view(),name='login'),
    path('logout',views.logout,name='logout'),
    path('search/',views.search,name='search'),
    path('update.html',views.Update.as_view(),name='update'),
    path('equipment_parameter/<int:page>.html',views.equipment_parameter,name='equipment_parameter'),
    path('management.html', views.management,name='mian_html'),
]