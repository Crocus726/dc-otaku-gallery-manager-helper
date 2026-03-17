import sys
import os
import atexit
import traceback
from datetime import datetime

class TimeLogger:
    def __init__(self, filename):
        self.terminal = sys.stdout
        self.log = open(filename, "a", encoding = "utf-8")
        self.is_new_line = True

    def write(self, message):
        if message == '\n':
            self.terminal.write(message)
            self.log.write(message)
            self.log.flush()
            self.is_new_line = True
            return
        if self.is_new_line:
            now = datetime.now().strftime("[%Y-%m-%d %H:%M:%S] ")
            self.terminal.write(now)
            self.log.write(now)
            self.is_new_line = False
        self.terminal.write(message)
        self.log.write(message)
        self.log.flush()
        
    def flush(self):
        pass

def on_exit():
    print("프로그램 종료")

def setup_logger():
    if not os.path.exists("logs"):
        os.makedirs("logs")
    log_start_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_filename = f"logs/log_{log_start_time}.txt"

    logger = TimeLogger(log_filename)
    sys.stdout = logger
    sys.stderr = logger
    atexit.register(on_exit)

    return log_filename
