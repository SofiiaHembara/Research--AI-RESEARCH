from collections import Counter
from itertools import islice

def find_film_keywords(film_keywords: dict, film_name: str):
    return {key for key, value in film_keywords.items() if film_name in value}

def find_films_with_keywords(film_keywords: dict, num_of_films: int):
    film_counter = Counter(film for keywords in film_keywords.values() for film in keywords)
    sorted_films = sorted(film_counter.items(), key=lambda x: (-x[1], x[0]))
    return list(islice(sorted_films, num_of_films))