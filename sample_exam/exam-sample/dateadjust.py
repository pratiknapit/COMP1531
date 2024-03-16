from datetime import date, datetime, timedelta

def adjust(weeks, hours, string):

    if weeks > 50 or hours > 50:
        raise ValueError

    date_string = string

    date_object = datetime.strptime(date_string, "%H:%M on %d %B %Y")

    date_add = date_object + timedelta(weeks = weeks)

    date_add = date_add + timedelta(hours = hours)

    date_str = date_add.strftime("%H:%M on %-d %B %Y")

    return date_str

adjust(4, 4, "16:40 on 28 January 2021")