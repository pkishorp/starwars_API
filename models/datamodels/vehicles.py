from models.basemodel import Base
from typing import List, Optional

class Vehicle_(Base):

    name: str
    model: str
    vehicle_class: str
    manufacturer: str
    length: str
    cost_in_credits: str
    crew: str
    passengers: str
    max_atmosphering_speed: str
    cargo_capacity: str
    consumables: str

    pilots: Optional[List[str]]


if __name__ == '__main__':
    external = {
    "name": "Sand Crawler",
    "model": "Digger Crawler",
    "manufacturer": "Corellia Mining Corporation",
    "cost_in_credits": "150000",
    "length": "36.8 ",
    "max_atmosphering_speed": "30",
    "crew": "46",
    "passengers": "30",
    "cargo_capacity": "50000",
    "consumables": "2 months",
    "vehicle_class": "wheeled",
    "pilots": [],
    "films": [
        "https://swapi.dev/api/films/1/",
        "https://swapi.dev/api/films/5/"
    ],
    "created": "2014-12-10T15:36:25.724000Z",
    "edited": "2014-12-20T21:30:21.661000Z",
    "url": "https://swapi.dev/api/vehicles/4/"
    }

    obj = Vehicle_(**external)
    print(obj)

