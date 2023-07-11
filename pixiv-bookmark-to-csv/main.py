from utils.logger import init_logger
from utils.pixiv import init_api


class AppClass:
    def __init__(self):
        self.logger = init_logger()

    def main(self):
        self.logger.info("This is the main function.")

        # Initialize the API.
        self.api = init_api(self)


if __name__ == "__main__":
    app = AppClass()
    app.main()
