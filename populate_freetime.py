import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'freetime_project.settings')
import django
django.setup()
from freetime.models import Profile, Activity, Category, Goal, Record
import datetime


def populate():
    add_profile(user_name="Spacefish",
                created_date=datetime.date(2015, 5, 10),
                last_active=datetime.datetime(2015, 5, 12, 11, 3),
                )

    add_profile(user_name="Scotro",
                created_date=datetime.datetime(2015, 5, 12),
                last_active=datetime.datetime(2015, 5, 12, 9, 14),
                )

    add_activity(name="Writing",
                 user_starred=True,
                 sessions=50,
                 last_session=datetime.datetime(2015, 3, 20, 16, 30, 0),
                 )

    add_activity(name="Exercise",
                 user_starred=True,
                 sessions=8,
                 last_session=datetime.datetime(2015, 5, 10, 10, 15),
                 )

    add_activity(name="Reading",
                 user_starred=True,
                 sessions=25,
                 last_session=datetime.datetime(2015, 4, 30, 1800, 0, 0),
                 )

    add_activity(name="Bicycling",
                 user_starred=False,
                 sessions=0,
                 last_session=None,
                 )

    add_activity(name="Cooking",
                 user_starred=False,
                 sessions=0,
                 last_session=None,
                 )

    add_category(name="Health")


def add_profile(user_name, created_date, last_active):
    profile = Profile.objects.get_or_create()[0]
    profile.user_name = user_name
    profile.created_date = created_date
    profile.last_active = last_active

    profile.save()

    return profile


def add_activity(name, user_starred, sessions, last_session):
    activity = Activity.objects.get_or_create()[0]
    activity.name = name
    activity.user_starred = user_starred
    activity.sessions = sessions
    activity.last_session = last_session

    activity.save()

    return activity


def add_category(name):
    category = Category.objects.get_or_create()[0]
    category.name = name

    category.save()

    return category


def add_goal(name, activity, user_goal):
    goal = Goal.objects.get_or_create()[0]
    goal.name = name
    goal.activity = activity
    goal.user_goal = user_goal

    goal.save()

    return goal


def add_record(activity, date, personal_best):
    record = Record.objects.get_or_create()[0]
    record.activity = activity
    record.date = date
    record.personal_best = personal_best

    record.save()

    return record


if __name__ == '__main__':
    print "Starting Freetime population script..."
    populate()