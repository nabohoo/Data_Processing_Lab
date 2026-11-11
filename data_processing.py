import csv, os
class Dataloader:
    def __init__(self,filename):
        self.filename = filename
    def covert_to_table(self):
        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))

        cities = []
        with open(os.path.join(__location__, self.filename)) as f:
            rows = csv.DictReader(f)
            for r in rows:
                cities.append(dict(r))
        return cities
# 1 filer by keyword
# 2 avg
# 3 filter by tempeture
# 4 max tempeute
# 6 unique contry
class table:
    def __init__(self,data):
        self.data = data
    def filter_by_keyword(self,keyword):
        result = []
        for city in self.data:
            if city['country'] == keyword:
                result.append(city)
        return result
    def filter_by_temperature_over(self,num):
        result = []
        for city in self.data:
            if float(city['temperature']) > int(num):
                result.append(city['city'])
        return result
    def avg(self,dict_list):
        total = []
        for city in dict_list:
            total.append(float(city['temperature']))
        result_avg = sum(total)/len(total)
        return result_avg
    def max_tempurature(self,dict_list):
        total = []
        for city in dict_list:
            total.append(float(city['temperature']))
        result_max = max(total)
        return result_max
    def unique_count(self):
        count = 0
        country_list = []
        for city in self.data:
            if city['country'] not in country_list:
                country_list.append(city['country'])
                count+= 1
        return count
# {'city': 'Aalborg', 'country': 'Denmark', 'latitude': '57.03', 'longitude': '9.92', 'temperature': '7.52'}
# {'city': 'Aberdeen', 'country': 'United Kingdom', 'latitude': '57.17', 'longitude': '-2.08', 'temperature': '8.10'

#  do the result
load_data = Dataloader('Cities.csv')
my_tables = load_data.covert_to_table()
mytable = table(my_tables)
# Print the average temperature of all the cities
average_all = mytable.avg(mytable.data)
print(f"The average temperature of all cities is: {average_all}")

# Print all cities in Germany
Germany_city = mytable.filter_by_keyword("Germany")
print(Germany_city)

# Print all cities in Spain with a temperature above 12°C
Spain_city = mytable.filter_by_keyword("Spain")
Spian_12 = mytable.filter_by_temperature_over(12)
print(Spian_12)

# Count the number of unique countries
unique_cout = mytable.unique_count()
print(unique_cout)


# Print the average temperature for all the cities in Germany
Germany_avg = mytable.avg(Germany_city)
print(Germany_avg)

# Print the max temperature for all the cities in Italy
Italy_city = mytable.filter_by_keyword("Italy")
max_Italy = mytable.max_tempurature(Italy_city)
print(max_Italy)