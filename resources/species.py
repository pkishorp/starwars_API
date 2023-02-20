from resources.base import ResourceBase
from Utils.fetch_data import hit_url


class Species(ResourceBase):
    """
        film class base related functionality
    """

    def __init__(self):
        super().__init__()
        self.relative_url = "/api/species"

    def get_count(self):
        complete_url = self.home_url + self.relative_url
        response = hit_url(complete_url)
        data = response.json()
        count = data.get("count")
        return count