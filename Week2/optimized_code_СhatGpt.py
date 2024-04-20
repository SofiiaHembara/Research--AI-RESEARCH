import time
import resource

from memory_profiler import profile
# @profile
def read_file(file_path: str) -> dict:
    """
    Read file and return a dictionary
    """
    with open(file_path, 'r', encoding='UTF-8') as file:
        next(file)  # Skip header
        return {line.split(',')[0]: int(line.split(',')[1]) for line in file}
# @profile
def rescue_people(smarties, limit_iq):
    """
    Returns a number of trips and lists of persons in one trip.
    """
    if not smarties:
        return (0, [])
    
    # Sort smarties by IQ in descending order
    sorted_smarties = sorted(smarties.items(), key=lambda x: (-x[1], x[0]))
    
    trips = []
    remaining_people = set(sorted_smarties)
    
    while remaining_people:
        trip, total_iq = [], 0
        for name, iq in sorted_smarties:
            if (name, iq) in remaining_people and total_iq + iq <= limit_iq:
                trip.append(name)
                total_iq += iq
                remaining_people.remove((name, iq))
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

#Elapsed time: 1.5020370483398438e-05 seconds
# Memory used: 45662208 kilobytes