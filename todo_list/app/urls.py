from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name="todo"),
    path('del/<str:item_id>', views.delete, name="del"),
    path('detail/<int:item_id>/', views.detail, name='detail'),
    path('edit/<int:item_id>/', views.edit_item, name='edit_item'),
]