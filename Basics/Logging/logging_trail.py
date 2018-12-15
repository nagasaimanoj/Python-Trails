import logging

# one time config. cant change in run-time
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',  # log msg format
    # filename='example.log',  # to save logs to file
    level=logging.DEBUG,  # can set any int. default = WARNING(ie, 30)
    datefmt='%Y-%m-%d %H:%M:%S'  # date-time format. only applicable for custom formats
)

"""
levels of priority

50 - CRITICAL
40 - ERROR
30 - WARNING
20 - INFO
10 - DEBUG

each level can print it's level & the levels below it
i.e., log level 10 can be printed in all 5 loggers
& logger set to 50 can save all 5 types of logs
"""

log_str = 'something to log'

# using pre-defined log funcs
logging.critical(log_str)
logging.error(log_str)
logging.warning(log_str)
logging.info(log_str)
logging.debug(log_str)

# using log func
logging.log(logging.INFO, log_str)

# using custom log-levels
logging.log(91, log_str)

# custom log-levels in [10, 20, 30, 40, 50] gets replaced with pre-defined log level names
logging.log(10, log_str)

# if __name__ == '__main__' this will assume this prog was runnig by root
