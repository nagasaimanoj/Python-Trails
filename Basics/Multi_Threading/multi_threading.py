import _thread  # most basic way to use multi-threading in python


def print_time(thread_num):
    """ a function to parallel process"""
    for _ in range(10):
        # this prints a thread number in its own line vertically
        print('\t' * thread_num, str(thread_num))


try:
    for i in range(10):
        # start_new_thread accepts func & its parameters as input and starts that func right away
        _thread.start_new_thread(print_time, (i, ))
except:
    print('Error: unable to start thread')
