from django.shortcuts import render
from django.http import HttpResponse

class Game: 
  def __init__(self, name, description, number):
    self.name = name
    self.description = description
    self.number = number

games = [
  Game('Pinata', 'Hit it!', 20),
  Game('JackBox Games', 'Virtual games you can play anywhere with anyone!', 8),
  Game('Unwrap the Saran Wrap', 'Find the prizes within the saran wrap!', 10)
]

def home(request):
  return HttpResponse('<h1>Welcome to the Party Game Planner</h1>')

def about(request):
  return render(request, 'about.html')

def games_index(request):
  return render(request, 'games/index.html', { 'games': games })



