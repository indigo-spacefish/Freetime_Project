import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'freetime_project.settings')
import django
django.setup()
import datetime
from freetime.models import Profile, Activity, Category, Goal, Record


H = "health"
P = "personal_development"
E = "entertainment"
A = "activity"


def populate():
    add_profile(
        user_name="Spacefish",
        created_date=datetime.datetime.utcnow(),
        last_active=datetime.datetime.utcnow(),
        )

    add_profile(
        user_name="Scotro",
        created_date=datetime.datetime.utcnow(),
        last_active=datetime.datetime.utcnow(),
        )

    health = add_category(
        name=H,
        )

    personal_development = add_category(
        name=P,
        )

    entertainment = add_category(
        name=E,
        )

    writing = add_activity(
        name="writing",
        categories=[personal_development],
        user_starred=True,
        sessions=5,
        last_session=datetime.datetime.utcnow(),
        )

    exercise = add_activity(
        name="exercise",
        categories=[health],
        user_starred=True,
        sessions=2,
        last_session=datetime.datetime.utcnow(),
        )

    reading = add_activity(
        name="reading",
        categories=[entertainment, personal_development],
        user_starred=True,
        sessions=2,
        last_session=datetime.datetime.utcnow(),
        )

    bicycling = add_activity(
        name="bicycling",
        categories=[health],
        user_starred=False,
        sessions=0,
        last_session=None,
        )

    cooking = add_activity(
        name="cooking",
        categories=[health, personal_development],
        user_starred=False,
        sessions=0,
        last_session=None,
        )

    video_games = add_activity(
        name="video_games",
        categories=[entertainment],
        user_starred=True,
        sessions=10,
        last_session=datetime.datetime.utcnow(),
        )

    add_goal(
        name="write_more",
        activity=writing,
        user_goal=True,
        option_type=2,
        )

    add_goal(
        name="game_less",
        activity=video_games,
        user_goal=True,
        option_type=3,
        )

    add_goal(
        name="cook_more",
        activity=cooking,
        user_goal=False,
        option_type=1,
        )

    add_goal(
        name="reading_goal",
        activity=reading,
        user_goal=True,
        option_type=4,
        )

    make_records()


def add_profile(user_name, created_date, last_active):
    profile = Profile.objects.get_or_create(
        user_name=user_name,
        created_date=created_date,
        last_active=last_active,
    )[0]

    return profile


def add_category(name):
    category = Category.objects.get_or_create(
        name=name,
    )[0]

    return category


def add_activity(name, categories, user_starred, sessions, last_session):
    if not Activity.objects.filter(name=name) in Activity.objects.all():
        activity = Activity.objects.get_or_create(
            name=name,
            defaults={
                'categories': categories,
                'user_starred': user_starred,
                'sessions': sessions,
                'last_session': last_session,
            }
        )[0]

        return activity


def add_goal(name, activity, user_goal, option_type):
    goal = Goal.objects.get_or_create(
        activity=activity,
        name=name,
        user_goal=user_goal,
        option_type=option_type,
    )[0]

    return goal


def add_record(activity, date, personal_best):
    record = Record.objects.get_or_create(
        activity=activity,
        date=date,
        personal_best=personal_best,
    )[0]

    return record


def make_records():
    for activity in Activity.objects.all():
        record_count = activity.sessions
        now = datetime.datetime.utcnow()
        incrementer = 1

        for x in range(0, record_count):
            add_record(activity=activity,
                       date=(now - datetime.timedelta(days=incrementer)),
                       personal_best=False,
                       )
            incrementer += 1


def make_general_category():
    Category.objects.get_or_create(name="General")


if __name__ == '__main__':
    print "Starting Freetime population script..."
    make_general_category()
    populate()

    # Instrumentation
    print Profile.objects.all()
    print Category.objects.all()
    print Activity.objects.all()
    print Goal.objects.all()