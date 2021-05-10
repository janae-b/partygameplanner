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
from .models import Game, Plan, Photo

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
  plans_games_arent_played = Plan.objects.exclude(id__in = game.plans.all().values_list('id'))
  party_form = PartyForm()
  return render(request, 'games/detail.html', { 'game': game, 'party_form': party_form, 'plans': plans_games_arent_played })
  

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
def assoc_plan(request, game_id, plan_id):
  Game.objects.get(id=game_id).plans.add(plan_id)
  return redirect('detail', game_id=game_id)

@login_required
def add_party(request, game_id):
  form = PartyForm(request.POST)
  if form.is_valid():
    new_party = form.save(commit=False)
    new_party.game_id = game_id
    new_party.save()
  return redirect('detail', game_id=game_id)

class PlanList(LoginRequiredMixin, ListView):
  model = Plan

class PlanDetail(LoginRequiredMixin, DetailView):
  model = Plan

class PlanCreate(LoginRequiredMixin, CreateView):
  model = Plan
  fields = '__all__'

class PlanUpdate(LoginRequiredMixin, UpdateView):
  model = Plan
  fields = ['name', 'difficulty']

class PlanDelete(LoginRequiredMixin, DeleteView):
  model = Plan
  success_url = '/plans/'

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

@login_required
def add_photo_plan(request, plan_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, plan_id=plan_id)
      photo.save()
    except Exception as err:
      print('An error occurred uploading file to S3: %s' % err)
  return redirect('detail', plan_id=plan_id)

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


