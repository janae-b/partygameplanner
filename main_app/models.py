from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

EMOJIS = (
      ('A', '🍬'),
      ('Y', '🎲'),
      ('M', '🔮'),
      ('H', '🎩'),
      ('E', '🥳'),
      ('R', '🙌'),
      ('P', '🪅'),
      ('B', '🎂'),
      ('T', '🎊'),
      ('S', '🤩'),
      ('1', '👾'),
      ('2', '😎'),
      ('3', '🥸'),
      ('4', '🎈'),
      ('5', '🎁'),
      ('6', '👑'),
      ('7', '📝')
)

WHERE = (
  ('O', 'Outdoors'),
  ('I', 'Indoors'),
  ('B', 'Both'),
  ('V', 'Virtual')
)

class Plan(models.Model):
  name = models.CharField(max_length=50)
  emoji = models.CharField(max_length=1,
    choices=EMOJIS,
    default=EMOJIS[0][0]
  )


  def __str__(self):
    return f"{self.get_emoji_display()} on {self.emoji}"

  def get_absolute_url(self):
    return reverse("plans_detail", kwargs={"pk": self.id})
  

class Game(models.Model):
  name = models.CharField(max_length=100, help_text='</br>')
  description = models.CharField(max_length=250, help_text='</br>')
  instructions = models.TextField(max_length=350, help_text='</br>')
  materials = models.CharField(max_length=100, help_text='</br>')
  number = models.IntegerField(default=5)
  where = models.CharField(max_length=1, help_text='</br>',
    choices=WHERE,
    default=WHERE[0][0])
  plans = models.ManyToManyField(Plan)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
      return reverse("detail", kwargs={"game_id": self.id})

  def __str__(self):
    return f"{self.get_where_display()} on {self.where}"

class Party(models.Model):
  date = models.DateField('Party Date', default=date.today)
  name = models.CharField('Party Name',
    max_length=150
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
  
