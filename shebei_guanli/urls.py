from django.urls import path
from . import views
urlpatterns = [

    path('login.html',views.Login.as_view(),name='login'),
    path('logout',views.logout,name='logout'),
    path('update.html',views.Update.as_view(),name='update'),
    path('equipment_parameter/<int:page>.html',views.Equipment_parameter.as_view(),name='equipment_parameter'),
    path('management.html', views.management,name='mian_html'),
    path('edit/<str:editnumber>.html', views.edit,name='edit'),
    path('test/', views.test),

]