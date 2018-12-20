from django.db import models


class SpainPortugal(models.Model):
    username = models.CharField(max_length=255, blank=False, null=False)
    followers = models.IntegerField(null=False, blank=False, default=0)
    following = models.IntegerField(null=False, blank=False, default=0)

    class Meta:
        ordering = ('-followers',)

    def __str__(self):
        return '%s, Followers: %d, following: %d' % (self.username, self.followers, self.following)


class NubePalabras(models.Model):
    keyword = models.CharField(max_length=255, blank=False, null=False)
    repeats = models.IntegerField(null=False, blank=False, default=0)

    class Meta:
        ordering = ('-repeats',)

    def __str__(self):
        return 'Keyword: %s, repeats: %d' % (self.keyword, self.repeats)


class FollowData(models.Model):
    nickname = models.CharField(max_length=255, blank=False, null=False)
    followers = models.IntegerField(null=False, blank=False, default=0)
    following = models.IntegerField(null=False, blank=False, default=0)
    ratio = models.FloatField(null=False, blank=False, default=0.0)

    class Meta:
        ordering = ('-ratio',)

    def __str__(self):
        return 'nickname: %s, followers: %d, following: %d, Followers/Following ratio: %.4f: ' % (self.nickname, self.followers, self.following, self.ratio)
