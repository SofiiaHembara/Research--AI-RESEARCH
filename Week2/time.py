import time
 
# record start time
start = time.time()
 
# define a sample code segment
"""
keyword_processor.py

This module provides functions for processing keywords associated with films.
"""

from collections import Counter
from itertools import islice

def find_film_keywords(film_keywords: dict, film_name: str) -> set:
    """
    Find keywords associated with a given film.

    Args:
        film_keywords (dict): A dictionary where keys are genres and values are lists of films.
        film_name (str): The name of the film to find keywords for.

    Returns:
        set: A set of genres associated with the given film name.

    Examples:
        >>> film_keywords = {
        ...     "Action": ["The Matrix", "Die Hard", "Terminator"],
        ...     "Adventure": ["Indiana Jones", "Pirates of the Caribbean", "Jurassic Park"],
        ...     "Sci-Fi": ["Star Wars", "Interstellar", "Inception"],
        ...     "Fantasy": ["Harry Potter", "Lord of the Rings", "The Hobbit"]
        ... }
        >>> find_film_keywords(film_keywords, "The Matrix")
        {'Action'}
    """
    return {key for key, value in film_keywords.items() if film_name in value}


def find_films_with_keywords(film_keywords: dict, num_of_films: int) -> list:
    """
    Find films with the most keywords.

    Args:
        film_keywords (dict): A dictionary where keys are genres and values are lists of films.
        num_of_films (int): The number of films to return.

    Returns:
        list: A list of tuples containing the top films with their associated keyword counts.

    Examples:
        >>> film_keywords = {
        ...     "Action": ["The Matrix", "Die Hard", "Terminator"],
        ...     "Adventure": ["Indiana Jones", "Pirates of the Caribbean", "Jurassic Park"],
        ...     "Sci-Fi": ["Star Wars", "Interstellar", "Inception"],
        ...     "Fantasy": ["Harry Potter", "Lord of the Rings", "The Hobbit"]
        ... }
        >>> find_films_with_keywords(film_keywords, 2)
        [('The Matrix', 1), ('Die Hard', 1)]
    """
    film_counter = Counter(film for keywords in film_keywords.values() for film in keywords)
    sorted_films = sorted(film_counter.items(), key=lambda x: (-x[1], x[0]))
    return list(islice(sorted_films, num_of_films))


dicti = {'USA': ['Dovbush', 'Top Gun: Maverick', 'Ticket to Paradise'], \
'Ukraine': ['Dovbush', 'Schedryk', 'Kruty 1918']}

print(find_film_keywords(dicti, 'Dovbush'))
print(find_films_with_keywords(dicti, 2))
 
# record end time
end = time.time()
 
# print the difference between start 
# and end time in milli. secs
print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")