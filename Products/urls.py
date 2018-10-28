from django.urls import path, include
from . import views

urlpatterns = [
    path('create/', views.create,name='create'),
    path('<int:Product_id>', views.detail, name='detail'),
    path('<int:Product_id>/upvote', views.upvote, name='upvote'),
]
