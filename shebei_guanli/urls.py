from django.urls import path
from . import views
urlpatterns = [

    path('login.html',views.Login.as_view(),name='login'),
    path('update.html',views.Update.as_view(),name='update'),
    path('Equipment_parameter/',views.Equipment_parameter.as_view(),name='equipment_parameter'),
    path('management.html', views.management,name='mian_html'),
]