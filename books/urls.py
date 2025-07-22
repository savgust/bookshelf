from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('add/', views.book_create, name='add_book'),
    path('<int:pk>/edit/', views.book_edit, name='edit_book'),
    path('<int:pk>/delete/', views.book_delete, name='delete_book'),
]
