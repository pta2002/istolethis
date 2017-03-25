from django.db import models
from django.utils import timezone
import uuid


class Game(models.Model):
    game_id = models.CharField(default=uuid.uuid4, max_length=36)
    created_at = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=256, default="Untitled")
    until = models.IntegerField(default=10)
    over = models.BooleanField(default=False)

    def __str__(self):
        return "%s: %s" % (self.game_id, self.title)

    def get_latest(self):
        return self.gametext_set.order_by('-submitted_at').first()

    def is_over(self):
        if self.until <= 0:
            return self.over
        return self.gametext_set.count() >= self.until or self.over


class GameText(models.Model):
    game = models.ForeignKey(Game)
    submitted_at = models.DateTimeField(default=timezone.now)
    text = models.TextField()

    def __str__(self):
        return self.text[:150]
