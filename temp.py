from datetime import datetime, time, timedelta
import time as tm
from functools import wraps

"""
time limiter to wait until reieve target datetime
0 is monday
"""

def time_limiter(function):
  @wraps(function)
  def wrap( *args, **kwargs):
        
        valid_weekdays = [0,1,2,5,6] 
        now_weekday = datetime.today().weekday()
        time_start = time(8,30)
        time_end = time(12,30)
        time_now = datetime.today().time()
        
        if (now_weekday in valid_weekdays and
                time_end > time_now > time_start ):
             return function( *args, **kwargs)
        
        if (datetime.now()+ timedelta(1)).weekday() in [3] :
            tm.sleep(244780) #this sleep to recieve saturday whan see 3(thursday) 
        
        if (datetime.now()+ timedelta(1)).weekday() in [4] :
            tm.sleep(15380) #this sleep to recieve saturday whan see 4(Friday) 

        tm.sleep(71980) # this sleep 20 hours to recieve next day 8:30   

  return wrap