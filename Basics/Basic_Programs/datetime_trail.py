from datetime import datetime

time_str = 'Thu Oct 11 2018 00:00:00 GMT 0530 (India Standard Time)'

time_format = '%a %b %d %Y %H:%M:%S %Z %f (India Standard Time)'

date_obj = datetime.strptime(
    date_string=time_str[:],
    format=time_format
)

print(date_obj)
