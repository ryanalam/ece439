from django.urls import path
from . import views

urlpatterns = [
    path('fibonacci/', views.index, name='index'),  # Start page
    path('calculate_fibonacci/', views.calculate_fibonacci, name='calculate_fibonacci'),  
    path('crud/',views.create,name='crud'),
    path('update/<int:id>/', views.edit,name='update'),
    path('delete/<int:id>/', views.delete, name='delete')
]
