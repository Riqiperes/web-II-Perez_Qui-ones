from django.urls import path

from . import views

urlpatterns = [
    path('', views.indexUsers, name='users'),  # Ruta con el nombre 'users'
    path('create/', views.createUserView, name='createUserView'),
    path('createUser/', views.createUser, name='createUser'),
    path('edit/<int:id>/', views.edit_user, name='editUser'),
    path('update/<int:id>/', views.update_user, name='updateUser'),
]