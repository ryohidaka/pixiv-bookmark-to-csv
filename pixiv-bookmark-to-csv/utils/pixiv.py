import time
from utils.config import REFRESH_TOKEN
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
