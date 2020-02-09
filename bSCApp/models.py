from django.db import models

# Create your models here.


class Race(models.Model):
    region = models.CharField(max_length=3)
    type = models.CharField(max_length=3)
    series = models.CharField(max_length=20)

    def __str__(self):
        return self.series


class User(models.Model):
    user_id = models.IntegerField()
    token = models.CharField(max_length=10)
    user_calendar = models.ForeignKey(Race, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_id


class Calendar(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE)

"""    
    def racesFromRegion(self, region):
        return self.race.region == region
"""