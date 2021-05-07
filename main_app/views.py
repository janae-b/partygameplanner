from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Game
from .forms import PlanningForm
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def games_index(request):
  games = Game.objects.all()
  return render(request, 'games/index.html', { 'games': games })

def games_detail(request, game_id):
  game = Game.objects.get(id=game_id)
  planning_form = PlanningForm()
  return render(request, 'games/detail.html', { 'game': game, 'planning_form': planning_form })

class GameCreate(CreateView):
  model = Game
  fields = '__all__'

class GameUpdate(UpdateView):
  model = Game
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['name', 'description', 'materials', 'instructions', 'number']

class GameDelete(DeleteView):
  model = Game
  success_url = '/games/'

def add_planning(request, game_id):
  # create a ModelForm instance using the data in request.POST
  form = PlanningForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_planning = form.save(commit=False)
    new_planning.game_id = game_id
    new_planning.save()
  return redirect('detail', game_id=game_id)

