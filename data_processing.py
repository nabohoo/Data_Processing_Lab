import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))


# Print first 5 cities only
for city in cities[:5]:
    print(city)

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = [float(city['temperature']) for city in cities]
print(sum(temps)/len(temps))
print()

# # Print all cities in Germany
print("All ciites in Gemany")
German_city =[]
for city in cities:
    if city['country'] == 'Germany':
        German_city.append(city['city'])
print(German_city)
print()

# Print all cities in Spain with a temperature above 12°C
'''
Your code here

'''
print("All ciites in Spain")
Spain_city =[]
for city in cities:
    if city['country'] == 'Spain' and float(city['temperature']) > 12:
        Spain_city.append(city['city'])
print(Spain_city)
print()


# Count the number of unique countries
'''
Your code here

'''
count = 0
lis_country =[]
for city in cities:
    if city['country'] not in lis_country:
        lis_country.append(city['country'])
        count+=1
print(f'Number of unique contries : {count}')
print()

# Print the average temperature for all the cities in Germany
'''
Your code here

'''
total = []
for city in cities:
    if city['country'] == 'Germany':
        total.append(float(city['temperature']))
avg_all = sum(total)/len(total)
print(f'Average temperature in Germany : {avg_all}')
print()


# Print the max temperature for all the cities in Italy
'''
Your code here

'''

total = []
for city in cities:
    if city['country'] == 'Italy':
        total.append(float(city['temperature']))
most_temp = max(total)
print(f'Max temperature in Italy : {most_temp}')
print()