import datetime, time

print(datetime.datetime.utcnow())
#returns the current time up to 1 second

def log(message, dt=datetime.datetime.utcnow()):
    print(dt, message)

# log('Start up')
def logs(*args):
    for arg in args:
        log(args)
        time.sleep(1)

