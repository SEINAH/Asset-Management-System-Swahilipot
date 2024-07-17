from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard-index'),
    path('new/', views.new, name='dashboard-new'),
    path('assets/', views.assets, name='dashboard-assets'),
    path('maintainance/', views.maintainance, name='dashboard-maintainance')
]
