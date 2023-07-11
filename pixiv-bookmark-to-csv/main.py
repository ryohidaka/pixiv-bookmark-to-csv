from utils.config import get_restrict
from utils.csv import get_last_id, output
from utils.logger import init_logger
from utils.pixiv import get_bookmarks, init_api


class AppClass:
    def __init__(self):
        self.logger = init_logger()

    def main(self):
        # Initialize the API.
        self.api = init_api(self)

        # Get the type of the target user.
        self.restrict = get_restrict()
        self.logger.info(f"Target: {self.restrict}")

        # Define the CSV file name.
        csv_file = f"output/{self.restrict}.csv"

        # Get the last ID registered in the CSV file.
        last_id = get_last_id(self, csv_file)

        # Get the list of bookmarks.
        bookmarks = get_bookmarks(self, last_id)

        # Output the list of users to the CSV file.
        output(self, csv_file, bookmarks)


if __name__ == "__main__":
    app = AppClass()
    app.main()
