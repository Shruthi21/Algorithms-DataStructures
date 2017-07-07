from datetime import datetime
from datetime import timedelta

def add_gigasecond(year,month,day):
    giga_seconds = 10 ** 9
    delta_time = (datetime)
    delta_seconds = 0
    my_datetime = datetime(year,month,day)
    current_datetime = datetime.now()

    delta_time = current_datetime - my_datetime
    delta_seconds = delta_time.days * 24 * 3600  +  delta_time.seconds + delta_time.microseconds/(10**6)
    print delta_seconds
    print giga_seconds
    if delta_seconds == giga_seconds:
        return True
    else:
        return False
    
    
    

    


    
