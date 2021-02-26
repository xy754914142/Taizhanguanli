from django.urls import path
from . import views
urlpatterns = [

    path('login.html',views.Login.as_view(),name='login'),
    path('logout',views.logout,name='logout'),
    path('update.html',views.Update.as_view(),name='update'),
    path('equipment_parameter/<str:shebei_type>/<int:page>.html',views.Equipment_parameter.as_view(),name='equipment_parameter'),
    path('edit/<str:shebei_type>/<str:editnumber>.html', views.Edit.as_view(),name='edit'),
    path('profile.html', views.Profile.as_view(),name='profile'),
    path('', views.index,name='index'),
    path('test/', views.test),

]