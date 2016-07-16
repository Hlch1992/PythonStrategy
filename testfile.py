from CorePython import queuing
from datetime import datetime
import os
from logging.handlers import TimedRotatingFileHandler
import logging
logger = logging.getLogger('generator')
loglocation = r'c:/users/Hlch1/logdir'
if not os.path.exists(loglocation):
    os.makedirs(loglocation)


fh = TimedRotatingFileHandler(os.path.join(loglocation, r'generator.txt'), when='m', interval=1,
                              backupCount=5, delay=False, utc=True)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
logger.setLevel(logging.DEBUG)

class FooClass(object):
    """My very first class: FooClass"""
    version = 1.0

    def __init__(self, nm='John Doe'):
        """constructor
        :rtype: object
        """
        self.name = nm
        print("created a class instance for', nm")
        self.past = datetime.now()
        self.present = datetime.now()










def main():
    fooclass=FooClass()

    myclass = queuing.MyClass()
    myclass.queuetest()


if __name__ == "__main__":
    logger.info('we are here in testfile {0}'.format(__name__))
    main()



