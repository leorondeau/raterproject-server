from django.db import models

class Game(models.Model):

    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    title = models.CharField("Title", on_delete=models.CASCADE)
    description = models.CharField(max_length=250)
    designer = models.CharField(max_length=50)
    year_released = models.DateField()
    number_of_players = models.CharField(max_length=10)
    estimated_time_of_play = models.IntegerField()
    age_recommendation = models.IntegerField()
    
