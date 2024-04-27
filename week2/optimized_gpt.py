import calendar as my_calendar
import sys
import time
import resource
def weekday_name(number: int) -> str:
    """
    Return a string representing a weekday
    (one of "mon", "tue", "wed", "thu", "fri", "sat", "sun")
    number : an integer in range [0, 6]
        
    >>> weekday_name(3)
    'thu'
    """
    weekdays = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    if 0 <= number <= 6:
        return weekdays[number]
    return None

def weekday(date: str) -> int:
    """
    Return an integer representing a weekday
    (0 represents Monday and so on)
    Read about algorithm as Zeller's Congruence
    date : a string of form "day.month.year"
    if the date is invalid raises AssertionError 
    with corresponding message
                                                
    >>> weekday("12.08.2015")
    2
    >>> weekday("28.02.2016")
    6
    """
    day, month, year = map(int, date.split("."))
    if month < 1 or month > 12 or day < 1:
        raise AssertionError("Invalid month or day")
    days_in_month = {
        4: 30, 6: 30, 9: 30, 11: 30,
        2: 29 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 28,
    }
    if day > days_in_month.get(month, 31):
        raise AssertionError(f"Invalid day for the given month ({days_in_month.get(month)} days)")
    if month > 12 or year < 1584:
        raise AssertionError("Invalid month or year")
    if month < 3:
        month += 12
        year -= 1
    k, j = year % 100, year // 100
    day_of_week = (day + 13 * (month + 1) // 5 + k + k // 4 + j // 4 - 2 * j) % 7
    return (day_of_week + 5) % 7

def calendar(month, year):
    """Return a string representing a horizontal calendar for the given month and year.

    month : an integer in range [1 , 12]
    year : an integer (strictly speaking the algorithm in weekday
           works correctly only for the Gregorian calendar, so year must
           be greater than 1583)
    when arguments are invalid raises AssertionError with corresponding message

    >>> print(calendar(8 , 2015))
    mon tue wed thu fri sat sun
                          1   2
      3   4   5   6   7   8   9
     10  11  12  13  14  15  16
     17  18  19  20  21  22  23
     24  25  26  27  28  29  30
     31
    """
    cal = my_calendar.month(year, month, w=3).lower().split('\n')[1:]
    return '\n'.join(cal).rstrip()

def transform_calendar(calendar: str) -> str:
    """Return a modified horizontal -> vertical calendar.

    calendar is a string of a calendar, returned by the calendar()
    function.
    >>> print(transform_calendar(calendar(5, 2002)))
    mon   6 13 20 27
    tue   7 14 21 28
    wed 1 8 15 22 29
    thu 2 9 16 23 30
    fri 3 10 17 24 31
    sat 4 11 18 25
    sun 5 12 19 26
    >>> print(transform_calendar(calendar(8 , 2015)))
    mon   3 10 17 24 31
    tue   4 11 18 25
    wed   5 12 19 26
    thu   6 13 20 27
    fri   7 14 21 28
    sat 1 8 15 22 29
    sun 2 9 16 23 30
    """
    splited_calendar = calendar.split('\n')
    new_days_column = [[] for _ in range(7)]
    for index, line in enumerate(splited_calendar):
        new_line = line.split()
        numbers = [item for item in new_line if item.isdigit()]
        length = len(numbers)
        if length == 0:
            days_column = splited_calendar[0].split()
            new_days_column = [[day] for day in days_column]
        if 0 < length <= 7:
            if index == len(splited_calendar) - 1:
                first_day = length
                for i in range(first_day):
                    new_days_column[i].append(numbers[i - first_day])
            else:
                first_day = 7 - length
                for i in range(first_day):
                    new_days_column[i].append(' ')
                for i in range(first_day, 7):
                    new_days_column[i].append(numbers[i - first_day])
    vertical_calendar = "\n".join(" ".join(day) for day in new_days_column)
    return vertical_calendar

def measure_memory_and_time():
    start_time = time.time()
    result = transform_calendar(calendar(8, 2015))
    end_time = time.time()
    elapsed_time = end_time - start_time
    memory_used = sys.getsizeof(result)
    print(f"The code executed in {elapsed_time} seconds.")
    usage = resource.getrusage(resource.RUSAGE_SELF)
    memory_used = usage.ru_maxrss
    print(f"The program used {memory_used} kilobytes of memory.")

measure_memory_and_time()
