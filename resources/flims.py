from resources.base import ResourceBase
from Utils.fetch_data import hit_url


class Film(ResourceBase):
    """
        film class base related functionality
    """

    def __init__(self):
        super().__init__()
        self.relative_url = "/api/films"

    def get_count(self):
        complete_url = self.home_url + self.relative_url
        response = hit_url(complete_url)
        data = response.json()
        count = data.get("count")
        return count
