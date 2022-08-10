from django.shortcuts import render
from .models import Show
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'home.html')

def shows_index(request):
  shows = Show.objects.all()
  return render(request, 'shows/index.html', { 'shows': shows})

def shows_detail(request, show_id):
  show = Show.objects.get(id=show_id)
  return render(request, 'shows/detail.html', { 'show': show})

class ShowCreate(CreateView):
  model = Show
  fields = '__all__'

class ShowUpdate(UpdateView):
  model = Show
  fields = ['category', 'description', 'watchTime']

class ShowDelete(DeleteView):
  model = Show
  success_url = '/shows/'