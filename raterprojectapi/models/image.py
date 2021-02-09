from django.db import models
from django.db.models.deletion import CASCADE

class Image(models.Model):

    game = models.ForeignKey("Game", on_delete=CASCADE)
    gamer = models.ForeignKey("Gamer", on_delete=CASCADE)
    image = models.ImageField(upload_to='Games', height_field=None, width_field=None, max_length=None)