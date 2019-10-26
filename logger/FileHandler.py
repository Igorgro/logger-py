class FileHandler:
    def __init__(self, filename):
        if not isinstance(filename, str):
            raise TypeError("expected string, not {}".format(type(filename)))
        else:
            if not filename.endswith("log"):
                raise ValueError("File name must ends with .log")
            else:
                self.filename = filename
                self.log_file = None

    def start(self):
        self.log_file = open(self.filename, "w")

    def log(self, log_str):
        self.log_file.write(log_str)

    def stop(self):
        self.log_file.close()