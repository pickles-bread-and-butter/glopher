import threading
import traceback
import logging
import sys


def thread_handler(args):
    if args.exc_type == SystemExit:
        return

    error_string = (
        f"Uncaught exception in thread {args.thread.name}:\n"
        f"Exception type: {args.exc_type.__name__}\n"
        f"Exception value: {args.exc_value}\n"
        f"Traceback:\n"
        f"{traceback.print_tb(args.exc_traceback)}"
    )
    raise Exception(error_string) 
