from django.shortcuts import render
from django.views.generic import (
    CreateView,
    ListView,
    DeleteView,
    UpdateView
)
from django.urls import reverse
from django.db.models import Q, Count
from .models import Todo
from .forms import TodoCreateForm
# Create your views here.

class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoCreateForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('todo-list')

    def get_context_data(self, **kwargs):
        context = super(TodoCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Todo'
        return context


class TodoListView(ListView):
    model = Todo
    ordering = ['-id']
    paginate_by = 50

    def get_paginate_by(self, queryset):
        return self.request.GET.get('per_page', self.paginate_by)

    def get_queryset(self):
        search_val = self.request.GET.get('search', '')
        new_context = Todo.objects.filter((Q(name__contains=search_val)))
        return new_context

    def get_context_data(self, **kwargs):
        context = super(TodoListView, self).get_context_data(**kwargs)
        context['title]'] = 'Todo'
        return context


class TodoUpdateView(UpdateView):
    model = Todo
    fields = ['name', 'category', 'is_completed']

    def get_success_url(self):
        return reverse('todo-list')

    def get_context_data(self, **kwargs):
        context = super(TodoUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Todo'
        return context


class TodoDeleteView(DeleteView):
    model = Todo

    def get_success_url(self):
        return reverse('todo-list')

    def get_context_data(self, **kwargs):
        context = super(TodoDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Todo Delete'
        return context


def dashboard(request):
    todo_obj = Todo.objects.aggregate(
        high=Count('category', filter=Q(category__name='High')),
        medium=Count('category', filter=Q(category__name='Medium')),
        low=Count('category', filter=Q(category__name='Low')),
    )
    context = {
        'High': todo_obj['high'],
        'Medium': todo_obj['medium'],
        'Low': todo_obj['low'],
    }

    return render(request, 'demo/dashboard.html', context)