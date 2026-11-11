import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

def filter_items(condition, dict_list):
    """
    Return a new list containing only the dictionaries that satisfy
    the given condition function.

    Args:
        condition: A function that takes a dictionary and returns True or False.
        dict_list: A list of dictionaries.

    Returns:
        A list of dictionaries for which condition(item) is True.

    Examples:
        >>> students = [
        ...     {"name": "Alice", "score": 90},
        ...     {"name": "Bob", "score": 70},
        ...     {"name": "Charlie", "score": 85}
        ... ]
        >>> filter_items(lambda s: s["score"] >= 85, students)
        [{'name': 'Alice', 'score': 90}, {'name': 'Charlie', 'score': 85}]

        >>> filter_items(lambda s: s["name"].startswith("A"), students)
        [{'name': 'Alice', 'score': 90}]

        >>> filter_items(lambda s: s["score"] > 100, students)
        []
    """
    # YOUR CODE HERE
    result_condition = []
    for city in dict_list:
        if condition(city):
            result_condition.append(city)

    return result_condition


def aggregate(aggregation_key, aggregation_function, dict_list):
    """
    Aggregate values associated with aggregation_key using the
    provided aggregation function.

    Args:
        aggregation_key: The dictionary key whose values should be aggregated.
        aggregation_function: A function such as sum, max, min, etc.
        dict_list: A list of dictionaries.

    Returns:
        The aggregated result.

    Examples:
        >>> students = [
        ...     {"name": "Alice", "score": 90},
        ...     {"name": "Bob", "score": 70},
        ...     {"name": "Charlie", "score": 85}
        ... ]

        >>> aggregate("score", sum, students)
        245

        >>> aggregate("score", max, students)
        90

        >>> aggregate("score", min, students)
        70

        >>> aggregate(
        ...     "score",
        ...     lambda scores: sum(scores) / len(scores),
        ...     students
        ... )
        81.66666666666667
    """
    # YOUR CODE HERE
    some_list = []
    for city in dict_list:
        some_list.append(city[aggregation_key])
    result = aggregation_function(some_list)
    print(result)


        
# Print the average temperature of all the cities
aggregate(
    'temperature',
    lambda temperature: sum(float(f) for f in temperature) / len(temperature) if len(temperature) > 0 else 0,
    cities
)
# Print all cities in Germany
print(filter_items(lambda s: s["country"] == 'Germany',cities))

# Print all cities in Spain with a temperature above 12°C
first = filter_items(lambda s: s["country"] == 'Spain',cities)
last_items = filter_items(lambda s: float(s['temperature']) > 12,first)
print(last_items)



# Count the number of unique countries
unique_coun = set(city['country'] for city in cities)
print(len(unique_coun))


# Print the average temperature for all the cities in Germany
german_city = filter_items(lambda s: s["country"] == 'Germany',cities)
aggregate(
    'temperature',
    lambda temperature: sum(float(f) for f in temperature) / len(temperature) if len(temperature) > 0 else 0,
    german_city
)
# Print the max temperature for all the cities in Italy
italy_city = filter_items(lambda s: s["country"] == 'Italy',cities)
aggregate(
    'temperature',
    lambda temperature:max(float(f) for f in temperature),
    italy_city
)
# g 1/Practice File/Term 2/Data_processing_lab/data_processing.py"'
# {'city': 'Aalborg', 'country': 'Denmark', 'latitude': '57.03', 'longitude': '9.92', 'temperature': '7.52'}
# {'city': 'Aberdeen', 'country': 'United Kingdom', 'latitude': '57.17', 'longitude': '-2.08', 'temperature': '8.10'