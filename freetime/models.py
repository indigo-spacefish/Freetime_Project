from django.db import models


class Profile(models.Model):
    user_name = models.CharField(max_length=255)
    created_date = models.DateTimeField()
    last_active = models.DateTimeField()

    def __unicode__(self):
        return self.user_name


class Activity(models.Model):
    name = models.CharField(max_length=255)
    user_starred = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Activities"


class Goal(models.Model):
    name = models.CharField(max_length=255)
    activity = models.ForeignKey(Activity)
    user_goal = models.BooleanField(default=False)

    def __unicode__(self):
        return self.goal_name


class Record(models.Model):
    activity = models.ForeignKey(Activity)
    date = models.DateTimeField()
    personal_record = models.BooleanField(default=False)

    def __unicode__(self):
        return self.activity.name + " Record"


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"