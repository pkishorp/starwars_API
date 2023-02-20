"""
1. TODO - import all resource classes here
2. TODO - get count of each resource
3. TODO - get singular resource URL from each resource
4. TODO - pull data from random 3 "singular" resource URLs
5. TODO - convert the script into CLI application
"""

from resources.flims import Film
from resources.planets import Planet
from resources.vehicles import Vehicle
from resources.species import Species
from resources.people import People
from resources.starships import Starship

if __name__ == '__main__':

    film_object = Film()
    total_films = film_object.get_count()

    planet_object = Planet()
    total_planet = planet_object.get_count()

    vehicle_object = Vehicle()
    total_vehicle = vehicle_object.get_count()

    species_object = Species()
    total_species = species_object.get_count()

    people_object = People()
    total_people = people_object.get_count()

    starships_object = Starship()
    total_starships = starships_object.get_count()

    print(f"total_films:==> {total_films}")
    print(f"total_planet:==> {total_planet}")
    print(f"total_vehicle:==> {total_vehicle}")
    print(f"total_starships:==> {total_starships}")
    print(f"total_species:==> {total_species}")
    print(f"total_people:==> {total_people}")



