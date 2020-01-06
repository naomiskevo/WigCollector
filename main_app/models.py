from django.db import models
from django.urls import reverse
from datetime import date

TREATMENTS = (
    ('L', 'Light'),
    ('M', 'Medium'),
    ('D', 'Deep'),

)

class Type(models.Model):
  part = models.CharField(max_length=50)
  make = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('types_detail', kwargs={'pk': self.id})


class Wig(models.Model):
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    length = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'wig_id': self.id})

    def conditioned_for_today(self):
        return self.condition_set.filter(date=date.today()).count() >= 1

class Condition(models.Model):
  date = models.DateField('condition date')
  treatment = models.CharField(
    max_length=1,
    choices=TREATMENTS,
    default=TREATMENTS[0][0]
  )
  wig = models.ForeignKey(Wig, on_delete=models.CASCADE)

  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_treatment_display()} on {self.date}"

  # change the default sort
  class Meta:
    ordering = ['-date']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    wig = models.ForeignKey(Wig, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for wig_id: {self.wig_id} @{self.url}"