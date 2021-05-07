from django.shortcuts import render
from django.http import HttpResponse

class Game: 
  def __init__(self, name):
    self.name = name


games = [
  Game('Pinata'),
  Game('JackBox Games'),
  Game('Unwrap the Saran Wrap')
]

def home(request):
  return HttpResponse('<h1>Welcome to the Party Game Planner</h1>')

def about(request):
  return render(request, 'about.html')

def games_index(request):
  return render(request, 'games/index.html', { 'games': games })



