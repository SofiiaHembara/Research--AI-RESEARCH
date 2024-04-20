import time
import resource

"""
Resque
"""
def read_file(file_path: str) -> dict:
    """
    Read file and return a dictionary
    >>> read_file('smart_people.txt')
    {'Elon Musk': 165, 'Mark Zuckerberg': 152, 'Will Smith': 157, \
'Marilyn vos Savant': 186, 'Judith Polgar': 170, 'Quentin Tarantino': 163, \
'Bill Gates': 160, "Conan O'Brien": 160, 'Emma Watson': 132, 'Barack Obama': 137}
    """
    with open(file_path, 'r', encoding='UTF-8') as file:
        lines = file.readlines()
        del lines[0]
        lst = [item.replace('\n', '') for item in lines]
        lst1 = [item.split(',')  for item in lst]
        people = {}
        for i in lst1:
            name = i[0]
            iq = i[1]
            people[name] = int(iq)
        return people

def sorting_values(smarties):
    """
    Sortes the values of the dictionary from largest to lowest.
    >>> sorting_values({"Steve Jobs": 160, "Albert Einstein": 160,\
"Sir Isaac Newton": 195, "Nikola Tesla": 189})
    [195, 189, 160, 160]
    """
    value_list = list(smarties.values())
    for i in range(len(value_list)):
        for j in range(len(value_list) - i - 1):
            if value_list[j] < value_list[j + 1]:
                value_list[j], value_list[j + 1] = value_list[j + 1], value_list[j]
    return value_list

def sorting_keys(smarties):
    """
    Sorts keys of the dictionary in lexicographic order.
    >>> sorting_keys({"Steve Jobs": 160, "Albert Einstein": 160,\
"Sir Isaac Newton": 195, "Nikola Tesla": 189})
    ['Albert Einstein', 'Nikola Tesla', 'Sir Isaac Newton', 'Steve Jobs']
    """
    keys_list = list(smarties.keys())
    for k in range(1, len(keys_list)):
        keys_to_insert = keys_list[k]
        s = k - 1
        while s >= 0 and keys_list[s] > keys_to_insert:
            keys_list[s + 1] = keys_list[s]
            s -= 1
        keys_list[s + 1] = keys_to_insert
    return keys_list

def rescue_people(smarties, limit_iq):
    """
    Returns a number of trips and lists of persons in one trip.
    >>> rescue_people({"Steve Jobs": 160, "Albert Einstein": 160,\
"Sir Isaac Newton": 195, "Nikola Tesla": 189},500)
    (2, [['Sir Isaac Newton', 'Nikola Tesla'], ['Albert Einstein', 'Steve Jobs']])
    """
    if not smarties:
        return (0, [])
    value_list = sorting_values(smarties)
    keys_list = sorting_keys(smarties)
    remaining_people = set(keys_list)
    trips = []
    while remaining_people:
        trip, total_iq = [], 0
        for iq in value_list:
            for name in keys_list:
                if name in remaining_people and smarties[name] == iq and total_iq + iq <= limit_iq:
                    trip.append(name)
                    total_iq += iq
                    remaining_people.remove(name)
                    break
        if trip:
            trips.append(trip)
        else:
            break
    return len(trips), trips

def measure_memory_and_time():
    start_time = time.time()
    result = rescue_people({"Steve Jobs": 160, "Albert Einstein": 160, "Sir Isaac Newton": 195, "Nikola Tesla": 189}, 500)
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    usage = resource.getrusage(resource.RUSAGE_SELF)
    memory_used = usage.ru_maxrss
    
    print(f"Elapsed time: {elapsed_time} seconds")
    print(f"Memory used: {memory_used} kilobytes")

if __name__ == '__main__':
    measure_memory_and_time()

# Elapsed time: 2.4080276489257812e-05 seconds
# Memory used: 7888896 kilobytes