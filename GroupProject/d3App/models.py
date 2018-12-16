from django.db import models


class SpainPortugal(models.Model):
    username = models.CharField(max_length=255, blank=False, null=False)
    followers = models.IntegerField(null=False, blank=False, default=0)
    following = models.IntegerField(null=False, blank=False, default=0)

    class Meta:
        ordering = ('-followers',)

    def __str__(self):
        return '%s, Followers: %d, following: %d' % (self.username, self.followers, self.following)
