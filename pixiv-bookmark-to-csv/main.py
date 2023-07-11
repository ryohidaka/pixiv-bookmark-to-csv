from utils.config import get_restrict
from utils.logger import init_logger
from utils.pixiv import init_api


class AppClass:
    def __init__(self):
        self.logger = init_logger()

    def main(self):
        self.logger.info("This is the main function.")

        # Initialize the API.
        self.api = init_api(self)

        # Get the type of the target user.
        self.restrict = get_restrict()
        self.logger.info(f"Target: {self.restrict}")


if __name__ == "__main__":
    app = AppClass()
    app.main()
