from django.db import models


GOAL_TYPE_OPTIONS = (
    (1, "Not a User Goal"),
    (2, "Increase Frequency"),
    (3, "Decrease Frequency"),
    (4, "Quantitative Goal"),
)


class Profile(models.Model):
    user_name = models.CharField(max_length=255, unique=True)
    created_date = models.DateTimeField("Date Created")
    last_active = models.DateTimeField("Last Active")

    def __unicode__(self):
        return self.user_name


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Activity(models.Model):
    name = models.CharField(max_length=255, unique=True)
    categories = models.ManyToManyField(Category)
    user_starred = models.BooleanField(default=False)
    sessions = models.IntegerField(default=0)
    last_session = models.DateTimeField("Most Recent Session", null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Activities"


class Goal(models.Model):
    name = models.CharField(max_length=255, unique=True)
    activity = models.ForeignKey(Activity)
    user_goal = models.BooleanField(default=False)
    option_type = models.IntegerField(default=1)

    def __unicode__(self):
        return self.goal_name


class Record(models.Model):
    activity = models.ForeignKey(Activity)
    date = models.DateTimeField("Activity Date")
    personal_best = models.BooleanField(default=False)

#    def get_personal_best(self):
#        if self.activity.user_starred:

    def __unicode__(self):
        return self.activity.name + " Record"