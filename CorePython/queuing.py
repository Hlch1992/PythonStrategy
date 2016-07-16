from collections import deque
from logging.handlers import TimedRotatingFileHandler
import logging
import os

logger = logging.getLogger('generator')


class MyClass(object):
    """My very first class: QueueClass"""
    def __init__(self):
        self.string = "hello world"
        logger.info("self string")
        logger.info('we are here in queueing {0}'.format(__name__))

    def queuetest(self):
        queue = deque(["Eric", "John", "Michael"])
        for x in queue:
            print(x)
        print(queue.pop())


def main():
    myClass = MyClass()
    myClass.queuetest()


if __name__ == "__main__":
    main()
