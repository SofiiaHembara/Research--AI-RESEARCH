from collections import deque
import time
import resource

def read_file(file_path: str) -> dict:
    """
    Read file and return a dictionary
    >>> read_file('smart_people.txt')
    {'Elon Musk': 165, 'Mark Zuckerberg': 152, 'Will Smith': 157, \
'Marilyn vos Savant': 186, 'Judith Polgar': 170, 'Quentin Tarantino': 163, \
'Bill Gates': 160, "Conan O'Brien": 160, 'Emma Watson': 132, 'Barack Obama': 137}
    """
    with open(file_path, 'r', encoding='UTF-8') as file:
        people = {}
        for line in file:
            if line.startswith('#'):
                continue
            name, iq = line.strip().split(',')
            people[name] = int(iq)
        return people

def rescue_people(smarties: dict, limit_iq: int) -> tuple[int, list]:
    """
    Returns a number of trips and lists of persons in one trip.
    >>> rescue_people({"Steve Jobs": 160, "Albert Einstein": 160,
    "Sir Isaac Newton": 195, "Nikola Tesla": 189}, 500)
    (2, [['Sir Isaac Newton', 'Nikola Tesla'], ['Albert Einstein', 'Steve Jobs']])
    """
    if not smarties:
        return 0, []

    people = deque(sorted(smarties.items(), key=lambda item: item[1], reverse=True))
    trips = []
    while people:
        trip, total_iq = [], 0
        while people and total_iq + people[0][1] <= limit_iq:
            name, iq = people.popleft()
            trip.append(name)
            total_iq += iq
        trips.append(trip)
    return len(trips), trips

print(rescue_people({"Steve Jobs": 160, "Albert Einstein": 160, "Sir Isaac Newton": 195, "Nikola Tesla": 189}, 500))

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

# Elapsed time: 5.9604644775390625e-06 seconds
# Memory used: 7737344 kilobytes