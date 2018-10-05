from time import (
    time,  # current epoch
    localtime,  # epoch -> struct_time obj
    strftime,  # struct_time obj -> datetime string
    strptime,  # datetime string -> struct_time obj
    mktime  # struct_time obj -> epoch
)

date_format = '%Y-%m-%d %H:%M:%S'

# current epoch
current_time_epoch = time()
print(current_time_epoch)

# epoch -> datetime string
current_time_str = strftime(
    date_format,
    localtime(current_time_epoch)
)
print(current_time_str)


# datetime string -> epoch
epoch = mktime(strptime(
    current_time_str,
    date_format
))
print(epoch)
