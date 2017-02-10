import datetime


def timestamp():
    return str(datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))
