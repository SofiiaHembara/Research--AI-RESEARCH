def find_film_keywords(film_keywords: dict, film_name: str):
  """
  Finds keywords associated with a specific film name.

  Args:
      film_keywords: A dictionary where keys are keywords and values are lists of film names.
      film_name: The name of the film to search for.

  Returns:
      A set of keywords associated with the film name.
  """
  return {key for key, value in film_keywords.items() if film_name in value}

def find_films_with_keywords(film_keywords: dict, num_of_films: int):
  """
  Finds the top N films with the most associated keywords.

  Args:
      film_keywords: A dictionary where keys are keywords and values are lists of film names.
      num_of_films: The number of films to return.

  Returns:
      A list of tuples containing (film_name, keyword_count) for the top N films.
  """
  # Create a dictionary with film names as keys and initial count as 0
  film_count = {film: 0 for film in sum(film_keywords.values(), [])}
  # Iterate through keywords and increment film counts
  for value in film_keywords.values():
      for film in value:
          film_count[film] += 1
  # Sort films by count in descending order, then by name alphabetically
  sorted_films = sorted(film_count.items(), key=lambda x: (-x[1], x[0]))
  # Return the top N films
  return sorted_films[:num_of_films]