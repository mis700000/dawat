'''Getting current time -: To translate a time instant from a seconds since the epoch floating-point value into a time-tuple, pass the floating-point value to a function (e.g., localtime) that returns a time-tuple with all nine items valid:'''
import time;
localtime = time.localtime(time.time())
print "Local current time :", localtime

import time;
localtime=time.localtime(time.time())
print "Local current time :",localtime
