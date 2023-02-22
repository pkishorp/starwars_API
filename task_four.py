"""
1. TODO - import all resource classes here
2. TODO - get count of each resource
3. TODO - get singular resource URL from each resource
4. TODO - pull data from random 3 "singular" resource URLs
5. TODO - convert the script into CLI application
"""

import argparse
from Utils.randgen import ProduceChars
from task_one import get_url
from Utils.fetch_data import hit_url
from pprint import pprint

# resource class
from resources.flims import Film
from resources.planets import Planet
from resources.vehicles import Vehicle
from resources.species import Species
from resources.people import People
from resources.starships import Starship
from resources.people import People

# pydantic classes(models)
from models.datamodels.people import People_
from models.datamodels.planets import Planet_
from models.datamodels.species import Specie_
from models.datamodels.starships import Starship_
from models.datamodels.films import Film_
from models.datamodels.vehicles import Vehicle_


# def films_data():
#     film_object = Film()
#     total_films = film_object.get_count()
#     print("Total films::", total_films)
#     film_data = film_object.get_sample_data()
#     film_data = Film_(**film_data)
#     print("Film data is ::", film_data)
#     film_urls = film_object.get_resource_urls()
#     print("Get all films urls::", film_urls)
#
#
# def planets_data():
#     planet_object = Planet()
#     total_planet = planet_object.get_count()
#     print("Total Planet::", total_planet)
#     planet_data = planet_object.get_sample_data()
#     planet_data = Planet_(**planet_data)
#     print("Planet data is ::", planet_data)
#     planet_urls = planet_object.get_resource_urls()
#     print("Get all planet urls::", planet_urls)
#
#
# def vehicles_data():
#     vehicle_object = Vehicle()
#     total_vehicle = vehicle_object.get_count()
#     print("Total Vehicle ::", total_vehicle)
#     vehicle_data = vehicle_object.get_sample_data(id_=4)
#     print("Vehicle data is::", vehicle_data)
#     vehicle_urls = vehicle_object.get_resource_urls()
#     print("Get all vehicle urls::", vehicle_urls)
#
#
# def specie_data():
#     species_object = Species()
#     total_species = species_object.get_count()
#     print("Total Species::", total_species)
#     species_data = species_object.get_sample_data()
#     species_data = Specie_(**species_data)
#     print("Species data::", species_data)
#     species_urls = species_object.get_resource_urls()
#     print("Get all species urls::", species_urls)
#
#
# def peoples_data():
#     people_object = People()
#     total_people = people_object.get_count()
#     print("Total People::", total_people)
#     people_data = people_object.get_sample_data()
#     people_data = People_(**people_data)
#     print("People data::", people_data)
#     people_urls = people_object.get_resource_urls()
#     print("Get all people url::", people_urls)
#
#
# def starship_data():
#     starships_object = Starship()
#     total_starships = starships_object.get_count()
#     print("Total Starships::", total_starships)
#     starships_data = starships_object.get_sample_data(id_=9)
#     starships_data = Starship_(**starships_data)
#     print("Starships data::", starships_data)
#     starship_urls = starships_object.get_resource_urls()
#     print("Get all starships url::", starship_urls)
#
#
# def main():
#     films_data()
#     planets_data()
#     starship_data()
#     vehicles_data()
#     peoples_data()
#     specie_data()
#

def random_data():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--limit",
                        default=3,type=int)
    parser.add_argument("-s", "--start",
                        default=1, type=int)
    parser.add_argument("-e", "--end",
                        default=100,type=int)
    parser.add_argument("-r", "--resource",
                        default="people",
                        choices=["people", "planets", "films", "species", "vehicles", "starships"]
                        )
    argument = parser.parse_args()
    print(f"parsed arguments are - {argument}")
    obj = ProduceChars(argument.start, argument.end, argument.limit)
    resources = [element for element in obj]
    output = []
    for serial_id in resources:
        print(f"Generating data for id:: {serial_id}")
        response_url = get_url(serial_id, argument.resource)
        data = hit_url(response_url)
        data = data.json()
        output.append(data)
        pprint(output)


if __name__ == "__main__":
    # main()
    random_data()





