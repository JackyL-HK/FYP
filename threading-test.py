# Threading example
# http://sebastiandahlgren.se/2014/06/27/running-a-method-as-a-background-thread-in-python/

import threading
import time

class ThreadingExample(object):
    """ Threading example class
    The run() method will be started and it will run in the background until the application exits.
    """
    def __init__(self, interval=1):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
        self.interval = interval

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        """ Method that runs forever """
        while True:
            print("I'm running in the background")
            time.sleep(self.interval)

example = ThreadingExample()
while True:
    time.sleep(3)
    print('every 3 secs')
    time.sleep(2)
    print('every 2 secs')
