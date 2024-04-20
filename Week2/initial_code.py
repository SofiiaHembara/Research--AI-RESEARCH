"""Analysis of movie titles by various keywords"""
def find_film_keywords(film_keywords: dict, film_name: str):

    """
    Finding keyword for input film name.
    >>> find_film_keywords({'USA': ['Tutanic', 'Top Gun: Maverick', 'Ticket to Paradise'], \
'Ukraine': ['Dovbush', 'Schedryk', 'Kruty 1918'], \
'France': ['La Vie en Rose', 'Amélie', 'La Grande Vadrouille']}, 'Dovbush')
    {'Ukraine'}
    """
    res = set()
    for key, value in film_keywords.items():
        for name in value:
            if film_name == name:
                res.add(key)
    return res
def find_films_with_keywords(film_keywords: dict, num_of_films: int):
    """
    Finding the top of films by number of keywords.
    >>> find_films_with_keywords({'USA': ['Dovbush', 'Top Gun: Maverick', 'Ticket to Paradise'], \
'Ukraine': ['Dovbush', 'Schedryk', 'Kruty 1918'], \
'France': ['La Vie en Rose', 'Amélie', 'La Grande Vadrouille']}, 2)
    [('Dovbush', 2), ('Amélie', 1)]
    """
    res = {}
    for value in film_keywords.values():
        for film in value:
            if film not in res:
                res[film] = 1
            else:
                res[film] += 1
    res_list = list(res.items())
    res_list = sorted(res_list, key=lambda x: x[1])[::-1]
    sorted_film_list = sorted(res_list, key=lambda x: (-x[1], x[0]))
    done_list = sorted_film_list[:num_of_films]
    return done_list
if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
