from enum import Enum
from datetime import datetime as dt

class LogLevel(Enum):
    INFO=1
    WARN=2
    ERROR=3

class Logger:
    def __init__ (self, *handlers):
        self.handlers = []
        for handler in handlers:
            self.add_handler(handler)

    def __enter__(self):
        print("__enter__")
        return self

    def add_handler(self, handler):
        self.handlers.append(handler)
        handler.start()

    def log (self, level=LogLevel.INFO, thread="MAIN", message=""):
        log_str = _logstring(level, thread, message)
        for handler in self.handlers:
            handler.log(log_str)

    def __exit__(self, exc_type, exc_value, traceback):
        for handler in self.handlers:
            handler.stop()
    
    def __del__(self):
        for handler in self.handlers:
            handler.stop()


    
def _logstring (level, thread, message):
    log_str = '['+dt.now().strftime('%Y-%m-%d %H:%M:%S')+']['
    if level == LogLevel.INFO:
        log_str += 'INFO'
    elif level == LogLevel.WARN:
        log_str += 'WARN'
    else:
        log_str += 'ERROR'
    log_str += ']['+thread+'] '+message+'\n'

    return log_str