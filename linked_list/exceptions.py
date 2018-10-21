"""Custom Exception"""


class LinkedListLoopException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)
