from django.urls import path

from todo_app.views import home_view, change_status, delete_task, edit_task_view, register_view, login_view, logout_view

urlpatterns = [
    path('', home_view, name='home'),
    path('change-status/<int:id>/', change_status, name='change-status'),
    path('delete/<int:id>', delete_task, name='delete-task'),
    path('edit-task/<int:id>/', edit_task_view, name='edit-task'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]