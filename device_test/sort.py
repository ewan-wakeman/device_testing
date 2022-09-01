#!/usr/bin/env python

import sys
from datetime import datetime
from typing import Iterable
from logzero import logger
from numpy import random

argv = sys.argv
default_len = 100


def get_argv():
    if len(sys.argv) > 1:
        try:
            rng_len = int(eval(argv[-1]))
        except Exception:
            rng_len = default_len
    else:
        rng_len = default_len
    return rng_len


def timeit(func):
    def wrap(*args, **kwargs):
        start = datetime.now()
        res = func(*args, **kwargs)
        end = datetime.now()
        logger.info(f"function {func.__name__} executed in {end-start}.")
        return res

    return wrap


@timeit
def create_range(length: int):
    return random.random(length)


@timeit
def sort_range(rng: Iterable):
    return sorted(rng)


if __name__ == "__main__":

    start = datetime.now()
    n_items = get_argv()
    logger.info(f"running with range of {n_items}")
    rng = create_range(n_items)
    sort = sort_range(rng)
    end = datetime.now()
    logger.info(f"script executed in {end-start}")
    sys.exit()
