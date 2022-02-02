from dataclasses import dataclass, field
import time
from typing import Callable, ClassVar, Dict, Optional

import logging

class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""

class SimpleTimer:
    def __init__(self):
        self._start_time = None

    def start(self):
        """Start a new timer"""
        self._start_time = None
        # if self._start_time is not None:
        #     raise TimerError(f"Timer is running. Use .stop() to stop it")

        self._start_time = time.perf_counter()

    def stop(self):
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")

        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        print(f"Elapsed time: {elapsed_time:0.4f} seconds")
        return elapsed_time

@dataclass 
class Timer:
    # Below are attributes on Timer - have default vals but can be specified when creating Timer 
    timers: ClassVar[Dict[str, float]] = dict() # Creates dict of all timers in single run (can use to send the dict to backend for storage - need a run ID to match up with other metrics in backend though!)
    num_format="{:0.4f}" # :0.4f is a format specifier: For toc - tic, print as decimal num w/ 4 decimals.
    text: str = f"Elapsed time for run: {num_format} seconds"
    _start_time: Optional[float] = field(default=None, init=False, repr=False)

    def start(self, name) -> None:
        """Start a new timer"""
        self.timers.setdefault(name, 0) # Appends timer name to timers dict
        if self._start_time is not None: # If timer is already started - raise error
            raise TimerError(f"Timer is running. Use .stop() to stop it")
        self._start_time = time.perf_counter() # uses some undefined point in time as its epoch - i.e., works with smaller numbers / is more accurate

    def stop(self, name, output_len=None) -> float:
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")

        length=''
        if output_len is not None: # [ Optional ] Return length of output in log if specified
            length = f' - Output Length: {output_len}'

        elapsed_time = time.perf_counter() - self._start_time # Calculate elapsed time
        logger_value = f'Task Name ({name}): {self.text}{length}'.format(elapsed_time)
        logging.debug(logger_value)
        self.timers[name] += elapsed_time # Appends time to timer name in dict

        # print(self.timers) # prints all the timers in a dict object
        self._start_time = None # set start time back to None

        return elapsed_time
