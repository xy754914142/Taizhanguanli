from django.urls import path
from . import views
urlpatterns = [
    path('update/',views.Update.as_view(),name='update')
]