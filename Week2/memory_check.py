import tracemalloc
 
# code or function for which memory
# has to be monitored
from collections import Counter
from itertools import islice

def find_film_keywords(film_keywords: dict, film_name: str):
    return {key for key, value in film_keywords.items() if film_name in value}

def find_films_with_keywords(film_keywords: dict, num_of_films: int):
    film_counter = Counter(film for keywords in film_keywords.values() for film in keywords)
    sorted_films = sorted(film_counter.items(), key=lambda x: (-x[1], x[0]))
    return list(islice(sorted_films, num_of_films))
 
# starting the monitoring
tracemalloc.start()
 
# function call

dicti = {
    "USA": ["Tutanic", "Top Gun: Maverick", "Ticket to Paradise"],
    "Ukraine": ["Dovbush", "Schedryk", "Kruty 1918"],
    "France": ["La Vie en Rose", "Amélie", "La Grande Vadrouille"],
}

print(find_film_keywords(dicti, "Amélie"))
print(find_films_with_keywords(dicti, 2))
 
# displaying the memory
print(tracemalloc.get_traced_memory())
 
# stopping the library
tracemalloc.stop()