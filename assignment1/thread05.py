# Starting a Thread
import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__== "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                datefmt="%H:%M:%S")

    logging.info("Main : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,))
    logging.info("Main : before running thread")
    x.start()
    logging.info("Main : wait for the thread to finish")
    # x.join()
    logging.info("Main : all done")

#ผลลัพธ์ที่ได้
#10:39:55: Main : before creating thread
#10:39:55: Main : before running thread
#10:39:55: Thread 1: starting
#10:39:55: Main : wait for the thread to finish
#10:39:55: Main : all done
#10:39:57: Thread 1: finishing

#ถ้าเอา comment บรรทัดที่ 21 ออกผลลัพธ์จะได้เป็นแบบนี้แทน
#11:18:07: Main : before creating thread
#11:18:07: Main : before running thread
#11:18:07: Thread 1: starting
#11:18:07: Main : wait for the thread to finish
#11:18:09: Thread 1: finishing
#11:18:09: Main : all done