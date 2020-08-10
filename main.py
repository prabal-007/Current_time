import time
import datetime

class Current_time(object):
    def __init__(self):
        self.date = str(datetime.datetime.fromtimestamp\              
            (time.time()).strftime('%d-%m-%Y %H:%M:%S'))     # first way
    def __repr__(self):
        return self.date

if __name__ == "__main__":
    print(Current_time())
    print(datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S'))       # second way
