from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import PlanningForm
from django.http import HttpResponse
import uuid
import boto3
from .models import Game, Event

S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'party-game-planner-jb'

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def games_index(request):
  games = Game.objects.all()
  return render(request, 'games/index.html', { 'games': games })

def games_detail(request, game_id):
  game = Game.objects.get(id=game_id)
  events_games_arent_played = Event.objects.exclude(id__in = game.events.all().values_list('id'))
  planning_form = PlanningForm()
  return render(request, 'games/detail.html', { 'game': game, 'planning_form': planning_form, 'events': events_games_arent_played })

class GameCreate(CreateView):
  model = Game
  fields = '__all__'

class GameUpdate(UpdateView):
  model = Game
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['name', 'description', 'materials', 'instructions', 'number', 'credit']

class GameDelete(DeleteView):
  model = Game
  success_url = '/games/'

def assoc_event(request, game_id, event_id):
  Game.objects.get(id=game_id).events.add(event_id)
  return redirect('detail', game_id=game_id)

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

class EventList(ListView):
  model = Event

class EventDetail(DetailView):
  model = Event

class EventCreate(CreateView):
  model = Event
  fields = '__all__'

class EventUpdate(UpdateView):
  model = Event
  fields = ['name', 'date']

class EventDelete(DeleteView):
  model = Event
  success_url = '/events/'

def add_photo(request, game_id):
  # photo-file will be the "name" attribute on the <input type="file">
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, game_id=game_id)
      photo.save()
    except Exception as err:
      print('An error occurred uploading file to S3: %s' % err)
  return redirect('detail', game_id=game_id)




