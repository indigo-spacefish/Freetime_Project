import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'freetime_project.settings')

import django
django.setup()

from freetime.models import Profile, Activity, Category, Goal, Record


def populate():
    pass


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