import platform
from .ConsoleHandler import ConsoleHandler
#TODO rewrite using PySerial
class SerialHandler(ConsoleHandler):
    def __init__(self, com_number):
        if not isinstance(com_number, int):
            raise TypeError("expected int, not {}".format(type(com_number)))
        else:
            if com_number < 0:
                raise ValueError("Invelid port number")
            else:
                if platform.system() == "Windows":
                    self.filename = "\\\\.\\COM"+str(com_number)
                elif platform.system() == "Linux":
                    self.filename = "/dev/ttyS"+str(com_number)
                self.log_file = None