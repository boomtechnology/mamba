# -*- coding: utf-8 -*-

from datetime import timedelta


class ExecutionContext(object):
    pass


class Runnable(object):

    def __init__(self):
        self.elapsed_time = timedelta(0)

    def execute(self, reporter, context):
        raise NotImplementedError
