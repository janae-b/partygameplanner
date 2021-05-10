from django.db import models
from django.urls import reverse
from datetime import date

PHASES = (
      ('M', 'Materials'),
      ('T', 'Test'),
      ('R', 'Ready to Play')
)

class Event(models.Model):
  name = models.CharField(max_length=50)
  date = models.DateField('complete date')

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse("events_detail", kwargs={"pk": self.id})
  

class Game(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  instructions = models.TextField(max_length=250)
  materials = models.CharField(max_length=100)
  number = models.IntegerField()
  credit = models.URLField()
  events = models.ManyToManyField(Event)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
      return reverse("detail", kwargs={"game_id": self.id})

class Planning(models.Model):
  date = models.DateField('complete date')
  phase = models.CharField(
    max_length=1,
    choices=PHASES,
    default=PHASES[0][0]
  )
  game = models.ForeignKey(Game, on_delete=models.CASCADE)  

  def __str__(self):
    return f"{self.get_phase_display()} on {self.date}"

  class Meta:
    ordering = ['-date']

class Photo(models.Model):
  url = models.CharField(max_length=200)
  game = models.ForeignKey(Game, on_delete=models.CASCADE)

  def __str__(self):
      return f"Photo for game_id: {self.game_id} @{self.url}"
  