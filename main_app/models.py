from django.db import models
from django.urls import reverse

PHASES = (
      ('M', 'Materials'),
      ('T', 'Test'),
      ('R', 'Ready to Play')
)

class Game(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  number = models.IntegerField()

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