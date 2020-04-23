import logging


class MedicalLogger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.propagate = False
        self.logger.setLevel(logging.INFO)
        self.formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(messages)s")

        self.levels = dict(
            DEBUG=logging.DEBUG,
            INFO=logging.INFO,
            WARNING=logging.WARNING,
            NOTSET=logging.NOTSET,
            ERROR=logging.ERROR,
            CRITICAL=logging.CRITICAL
        )
        return

    def add_stream_handler(self, level):
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(self.levels[level])
        stream_handler.setFormatter(self.formatter)

        self.logger.addHandler(stream_handler)

    def add_file_handler(self, file_name, mode, level):
        """
        :param file_name: .txt or .log
        :param mode: "w" / "a"
        :return:
        """
        file_handler = logging.FileHandler(file_name, mode=mode)
        file_handler.setLevel(self.levels[level])
        file_handler.setFormatter(self.formatter)

        self.logger.addHandler(file_handler)

    def __call__(self, *args, **kwargs):
        return self.logger
