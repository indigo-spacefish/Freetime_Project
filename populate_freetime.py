import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'freetime_project.settings')
import django
django.setup()
from freetime.models import Profile, Activity, Category, Goal, Record
import datetime
import pytz

local_tz = pytz.timezone('US/Pacific')

H = "health"
P = "personal_development"
E = "entertainment"
A = "activity"


def populate():
    add_profile(user_name="Spacefish",
                created_date=datetime.datetime(2015, 5, 10, tzinfo=local_tz),
                last_active=datetime.datetime.now(tz=local_tz),
                )

    add_profile(user_name="Scotro",
                created_date=datetime.datetime(2015, 5, 12, tzinfo=local_tz),
                last_active=datetime.datetime(2015, 5, 12, 9, 14, tzinfo=local_tz),
                )

    add_activity(name="writing",
                 categories=[P],
                 user_starred=True,
                 sessions=5,
                 last_session=datetime.datetime(2015, 3, 20, 20, 17, tzinfo=local_tz),
                 )

    add_activity(name="exercise",
                 categories=[H],
                 user_starred=True,
                 sessions=2,
                 last_session=datetime.datetime(2015, 5, 10, 10, 15, tzinfo=local_tz),
                 )

    add_activity(name="reading",
                 categories=[E, P],
                 user_starred=True,
                 sessions=2,
                 last_session=datetime.datetime(2015, 4, 30, 18, 0, tzinfo=local_tz),
                 )

    add_activity(name="bicycling",
                 categories=[H],
                 user_starred=False,
                 sessions=0,
                 last_session=None,
                 )

    add_activity(name="cooking",
                 categories=[H, P],
                 user_starred=False,
                 sessions=0,
                 last_session=None,
                 )

    add_activity(name="video_games",
                 categories=[E],
                 user_starred=True,
                 sessions=10,
                 last_session=datetime.datetime(2015, 5, 11, 22, 32, 15, tzinfo=local_tz),
                 )

    add_goal(name="write_more",
             activity="writing",
             user_goal=True,
             option_type=2,
             )

    add_goal(name="game_less",
             activity="video_games",
             user_goal=True,
             option_type=3,
             )

    add_goal(name="cook_more",
             activity="cooking",
             user_goal=False,
             option_type=1,
             )

    add_goal(name="reading_goal",
             activity="reading",
             user_goal=True,
             option_type=4,
             )

    make_records()

    for a in Activity.objects.all():
        print "Adding " + a.name

    for g in Goal.objects.all():
        print "Adding " + g.name


def add_profile(user_name, created_date, last_active):
    profile = Profile()
    profile.user_name = user_name
    profile.created_date = created_date
    profile.last_active = last_active

    profile.save()

    return profile


def add_category(name):
    category = Category()
    category.name = name

    category.save()

    return category


def add_activity(name, categories, user_starred, sessions, last_session):
    activity = Activity()
    activity.name = name
    activity.user_starred = user_starred
    activity.sessions = sessions
    activity.last_session = last_session

    activity.save()

    for c in categories:
        activity.categories.add(add_category(c))

    activity.save()

    return activity


# TODO change all foreign key relations from x.y = to add()
def add_goal(name, activity, user_goal, option_type):
    goal = Goal()
    goal.name = name
    goal.activity = Activity(activity)
    goal.user_goal = user_goal
    goal.option_type = option_type

    goal.save()

    return goal


def add_record(activity, date, personal_best):
    record = Record()
    record.activity = Activity(activity)
    record.date = date
    record.personal_best = personal_best

    record.save()

    return record


def make_records():
    for activity in Activity.objects.all():
        record_count = activity.sessions
        now = datetime.datetime.now()
        incrementer = 1

        for x in range(0, record_count):
            add_record(activity=activity,
                       date=(now - datetime.timedelta(days=incrementer)),
                       personal_best=False,
                       )
            incrementer += 1


if __name__ == '__main__':
    print "Starting Freetime population script..."
    populate()