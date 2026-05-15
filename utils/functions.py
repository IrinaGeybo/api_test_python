from datetime import datetime, timedelta
import random



def generate_checkin_checkout_dates(checkin=None, checkout=None):
    random_days=random.randint(1, 60)
    today=datetime.now()
    

    if checkin is None:
        checkin = today + timedelta(days=random_days)
        checkin = checkin.strftime('%Y-%m-%d')

    if checkout is None:
        checkout_date = datetime.strptime(checkin, "%Y-%m-%d") + timedelta(days=random.randint(1, 60))
        checkout = checkout_date.strftime('%Y-%m-%d')

    return checkin, checkout


# datetime.now()  - объект datetime из текущей даты и времени


def generate_negative_checkin_dates(checkin=None, checkout=None):
    random_days=random.randint(-30, -1)
    today=datetime.now()

    if checkin is None:
        checkin = today + timedelta(days=random_days)
        checkin = checkin.strftime('%Y-%m-%d')
    if checkout is None:
        checkout_date = datetime.strptime(checkin, "%Y-%m-%d") + timedelta(days=random.randint(1, 60))
        checkout = checkout_date.strftime('%Y-%m-%d')

    return checkin, checkout