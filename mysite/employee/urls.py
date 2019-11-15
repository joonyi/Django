from django.urls import path
from . import views

urlpatterns = [
    path('', views.show),
    path('emp/', views.emp),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.delete),
    
]