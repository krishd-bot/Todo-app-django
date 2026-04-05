from django.urls import path
from . import views

urlpatterns = [
    path('todo/', views.home, name='home'),
    path('edit/<int:id>/', views.edit_task, name='edit'),
    path('delete/<int:id>/', views.delete_task, name='delete'),
    path('toggle/<int:id>/', views.toggle_task, name='toggle'),
    path('', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
