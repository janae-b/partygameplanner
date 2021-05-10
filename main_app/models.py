from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# PHASES = (
#       ('M', 'Materials'),
#       ('T', 'Test'),
#       ('R', 'Ready to Play')
# )

class Plan(models.Model):
  name = models.CharField(max_length=50)
  date = models.DateField('Date')
  

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse("plans_detail", kwargs={"pk": self.id})
  

class Game(models.Model):
  name = models.CharField(max_length=100, help_text="Enter the name")
  description = models.TextField(max_length=250, help_text="Enter a description of the game")
  instructions = models.TextField(max_length=250, 
  help_text="Enter your instructions", 
  default= '1. ')
  materials = models.CharField(max_length=100, help_text="Enter the materials you will need")
  number = models.IntegerField(default=5, help_text="Enter the number of people who can play")
  plans = models.ManyToManyField(Plan)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
      return reverse("detail", kwargs={"game_id": self.id})

class Party(models.Model):
  date = models.DateField('Party Date')
  name = models.CharField('Party Name',
    max_length=150
    # choices=PHASES,
    # default=PHASES[0][0]
  )

  game = models.ForeignKey(Game, on_delete=models.CASCADE)  

  def __str__(self):
    return f"{self.phase} on {self.date}"

  class Meta:
    ordering = ['-date']

class Photo(models.Model):
  url = models.CharField(max_length=200)
  game = models.ForeignKey(Game, on_delete=models.CASCADE)

  def __str__(self):
      return f"Photo for game_id: {self.game_id} @{self.url}"
  