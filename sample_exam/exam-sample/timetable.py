from datetime import date, time, datetime

# Given a list of dates and list of times, generate and returns a list of datetimes.

def timetable(dates, times):
    dt_list = []
    for d in dates:
        #date = datetime.date(dates)
        date = d
        for t in times: 
            #time = datetime.time(times)   
            time = t  
            combined = datetime.combine(date, time)
            dt_list.append(combined)
    
    sort_time = sorted(dt_list)

    return sort_time
