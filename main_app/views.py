from cmath import log
from django.shortcuts import render, redirect
from .models import Show
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Add the following import
from django.http import HttpResponse

# Define the home view
class Home(LoginView):
  template_name = 'home.html'

def shows_index(request):
  shows = Show.objects.all()
  return render(request, 'shows/index.html', { 'shows': shows})

def shows_detail(request, show_id):
  show = Show.objects.get(id=show_id)
  return render(request, 'shows/detail.html', { 'show': show})

def signup(request):
    error_message = ''
    if request.method == 'POST':
      form = UserCreationForm(request.POST)
      if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('shows_index')
      else:
        error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)


class ShowCreate(LoginRequiredMixin, CreateView):
  model = Show
  fields = [ 'title', 'category', 'description', 'watchTime']
  def form_valid(self, form):
    form.instance.user = self.request.user 
    return super().form_valid(form)


class ShowUpdate(LoginRequiredMixin, UpdateView):
  model = Show
  fields = ['category', 'description', 'watchTime']


class ShowDelete(LoginRequiredMixin, DeleteView):
  model = Show
  success_url = '/shows/'