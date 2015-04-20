from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=255)

    def __str__(self):
        return self.user_name


class Activity(models.Model):
    activity_name = models.CharField(max_length=255)

    def __str__(self):
        return self.activity_name


class Goal(models.Model):
    goal_name = models.CharField(max_length=255)
    activity = models.ForeignKey(Activity)

    def __str__(self):
        return self.goal_name


class History(models.Model):
    history_index = models.ForeignKey(User)