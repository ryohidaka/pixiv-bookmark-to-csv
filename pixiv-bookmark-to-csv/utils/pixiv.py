import time
from utils.config import REFRESH_TOKEN, USER_ID
from pixivpy3 import AppPixivAPI


def init_api(self) -> AppPixivAPI:
    """
    Initialize the API.

    Returns:
        AppPixivAPI: The API client.
    """

    self.logger.info("[Start] Initialize the API client.")

    refresh_token = REFRESH_TOKEN

    api = AppPixivAPI()
    api.auth(refresh_token=refresh_token)
    time.sleep(2)

    self.logger.info("[End] Initialize the API client.")

    return api


def get_bookmarks(self):
    """
    Get a list of bookmarks.
    """
    api = self.api
    logger = self.logger
    logger.info("[Start] Getting bookmark list")

    # Define a list to store bookmarks.
    bookmarks = []

    # Get a list of bookmarks.
    res = api.user_bookmarks_illust(USER_ID, restrict=self.restrict)
    time.sleep(5)

    while True:
        try:
            illusts = res.illusts

            for data in illusts:
                # Create a bookmark.
                bookmark = {
                    "id": data.id,
                    "title": data.title,
                    "type": data.type,
                    "user_id": data.user.id,
                    "user_name": data.user.name,
                }

                bookmarks.append(bookmark)

            next_url = res.next_url
            logger.info(f"Next URL: {next_url}")

            if next_url:
                next_qs = api.parse_qs(res.next_url)
                time.sleep(2)
                res = api.user_bookmarks_illust(**next_qs)
                time.sleep(2)
            else:
                break

        except Exception as e:
            logger.error("Failed to get the bookmark.:", str(e))
            break

    logger.info("[End] Getting bookmark list")

    return bookmarks
