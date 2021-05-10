from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PartyForm
from django.http import HttpResponse, HttpResponseRedirect
import uuid
import boto3
from .models import Game, Event, Photo

S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'party-game-planner-jb'

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def games_index(request):
  games = Game.objects.filter(user=request.user)
  return render(request, 'games/index.html', { 'games': games })

@login_required
def games_detail(request, game_id):
  game = Game.objects.get(id=game_id)
  events_games_arent_played = Event.objects.exclude(id__in = game.events.all().values_list('id'))
  party_form = PartyForm()
  return render(request, 'games/detail.html', { 'game': game, 'party_form': party_form, 'events': events_games_arent_played })
  

class GameCreate(LoginRequiredMixin, CreateView):
  model = Game
  fields = ['name', 'description', 'instructions', 'materials', 'number']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class GameUpdate(LoginRequiredMixin, UpdateView):
  model = Game
  fields = ['name', 'description', 'materials', 'instructions', 'number']

class GameDelete(LoginRequiredMixin, DeleteView):
  model = Game
  success_url = '/games/'

@login_required
def assoc_event(request, game_id, event_id):
  Game.objects.get(id=game_id).events.add(event_id)
  return redirect('detail', game_id=game_id)

@login_required
def add_party(request, game_id):
  form = PartyForm(request.POST)
  if form.is_valid():
    new_party = form.save(commit=False)
    new_party.game_id = game_id
    new_party.save()
  return redirect('detail', game_id=game_id)

class EventList(LoginRequiredMixin, ListView):
  model = Event

class EventDetail(LoginRequiredMixin, DetailView):
  model = Event

class EventCreate(LoginRequiredMixin, CreateView):
  model = Event
  fields = '__all__'

class EventUpdate(LoginRequiredMixin, UpdateView):
  model = Event
  fields = ['name', 'date']

class EventDelete(LoginRequiredMixin, DeleteView):
  model = Event
  success_url = '/events/'

@login_required
def add_photo(request, game_id):
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

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


