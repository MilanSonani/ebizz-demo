from django.urls import path, include
from .views import TodoCreateView, TodoListView, TodoUpdateView, TodoDeleteView
from . import views

urlpatterns = [
    path('start/', views.dashboard, name='dashboard'),
    path('todo/new', TodoCreateView.as_view(), name='add-todo'),
    path('todo/', TodoListView.as_view(), name='todo-list'),
    path('todo/<int:pk>/update/', TodoUpdateView.as_view(), name='update-todo'),
    path('todo/<int:pk>/delete/', TodoDeleteView.as_view(), name='delete-todo')
]
