import logging


class Logger:
    @staticmethod
    def log(message: str):
        logging.info(message)


logging.basicConfig(
    format="%(levelname)s %(message)s",
    level=logging.INFO,
    handlers=[logging.StreamHandler()],
)
