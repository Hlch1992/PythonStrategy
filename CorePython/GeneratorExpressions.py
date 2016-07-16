from datetime import datetime
import os
from logging.handlers import TimedRotatingFileHandler
import time
import logging
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
        self.loglocation = r'/home/zedekiah/data/generator/'
        self.fileread = r'/home/zedekiah/Documents/Chapter2Paragraph.txt'
        self.logger = logging.getLogger('generator')


    def init_logger(self):
        if not os.path.exists(self.loglocation):
            os.makedirs(self.loglocation)

        self.logger.setLevel(logging.DEBUG)
        fh = TimedRotatingFileHandler(os.path.join(self.loglocation, r'generator.txt'), when='m', interval=1,
                                      backupCount=5, delay=False, utc=True)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        fh.setLevel(logging.DEBUG)
        self.logger.addHandler(fh)

    def refactor(self):
        modtime = time.gmtime(os.path.getmtime(self.fileread))
        print (modtime)
        print(time.strftime('%Y%m%d%H%S',modtime))
        print (max(len(x.strip()) for x in open(self.fileread)))
        data = [line.strip() for line in open(self.fileread)]
        for x in data:
            print(x)

def main():
    print ("hello worlds")
    test = FooClass()
    test.refactor()
    filename = input('Enter a file name: ')

    for eachline in open(filename,'r'):
        print (eachline)

if __name__ == "__main__":
    main()