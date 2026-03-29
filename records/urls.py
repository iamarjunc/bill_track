from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('record/<int:pk>/', views.record_detail, name='record_detail'),
    path('add/', views.add_record, name='add_record'),
    path('search/', views.search_records, name='search_records'),  # 🔥 API
]