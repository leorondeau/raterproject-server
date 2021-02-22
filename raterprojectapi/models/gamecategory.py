from raterprojectapi.models.category import Category
from django.db import models


class GameCategory(models.Model):

    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name ="gamecategory")
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="gamecategory")
    


