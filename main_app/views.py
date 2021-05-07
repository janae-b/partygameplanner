from django.shortcuts import render
from .models import Game
from django.http import HttpResponse

# class Game: 
#   def __init__(self, name, description, number):
#     self.name = name
#     self.description = description
#     self.number = number

# games = [
#   Game('Pinata', 'Hit it!', 20),
#   Game('JackBox Games', 'Virtual games you can play anywhere with anyone!', 8),
#   Game('Unwrap the Saran Wrap', 'Find the prizes within the saran wrap!', 10)
# ]

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def games_index(request):
  games = Game.objects.all()
  return render(request, 'games/index.html', { 'games': games })

def games_detail(request, game_id):
  game = Game.objects.get(id=game_id)
  return render(request, 'games/detail.html', { 'game': game })



