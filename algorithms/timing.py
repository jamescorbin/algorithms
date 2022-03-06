import time
import functools
import logging

logger = logging.getLogger(name=__name__)

def timing(f):
    @functools.wraps(f)
    def wrap(*args, **kwargs):
        t0 = time.perf_counter()
        ret = f(*args, **kwargs)
        t1 = time.perf_counter()
        print(f"{f.__name__}: {t1-t0:.3e}")
        return ret
    return wrap
