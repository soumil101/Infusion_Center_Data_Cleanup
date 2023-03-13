import pandas as pd
import numpy as np
from datetime import datetime, date
import re

def convertTime(time):
    # skips the row if there is no value for the column
    if time is None or pd.isnull(time):
        return None

    # checks whether time given is given as 'HH:MM A/PM' or has date in front as well
    form = re.match(r'(\d{1,2}):(\d{2})(\s*[AP]M)', time)
    # executes this conditional if no date in front is present
    # the try/except handling is for cases where the AM/PM and time has a space between them
    # converts the time to a datetime object
    if form:
        try:
            time = pd.to_datetime(time, format='%I:%M%p')
        except ValueError:
            time = pd.to_datetime(time, format='%I:%M %p')
    # executes this if date in front is present
    else:
        try:
            time = pd.to_datetime(time, format='%Y-%m-%d %I:%M%p')
        except ValueError:
            time = pd.to_datetime(time, format='%Y-%m-%d %I:%M %p')
    
    # return time as a datetime.time object
    time = time.time()
    return time

def timeDifference(time1, time2):
    if time1 is None or time2 is None:
        return None
    # changes datetime.time objects into datetime.datetime objects to allow subtraction
    res = datetime.combine(date.min, time2) - datetime.combine(date.min, time1)
    # returns difference between times in minutes
    res = int(res.total_seconds() / 60)
    return res

def timeOfDay(dt):
    h = dt.hour
    if h <= 9:
        return 'Early Morning (6:00AM - 9:00AM)'
    elif h <= 12: 
        return 'Morning (9:00AM - 12:00PM)'
    else: 
        return 'Afternoon (12:00 PM - 4:00PM)'