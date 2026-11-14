import csv, os
from pathlib import Path

class DataLoader:
    """Handles loading CSV data files."""
    
    def __init__(self, base_path=None):
        """Initialize the DataLoader with a base path for data files.
        """
        if base_path is None:
            self.base_path = Path(__file__).parent.resolve()
        else:
            self.base_path = Path(base_path)
    
    def load_csv(self, filename):
        """Load a CSV file and return its contents as a list of dictionaries.
        """
        filepath = self.base_path / filename
        data = []
        
        with filepath.open() as f:
            rows = csv.DictReader(f)
            for row in rows:
                data.append(dict(row))
        
        return data

class DB:
    """Your code here"""
    def __init__(self):
        self.table = []

    def insert(self,tables_data):
        self.table.append(tables_data)

    def search(self,tables_name):
        for x in self.table:
            if x.table_name == tables_name:
                return x
        return None
    
    
class Table:
    """Your code here"""
    def __init__(self,table_name,table):
        self.table_name = table_name
        self.table = table

    def filter(self,condition):
        vaild_list =[]
        for row in self.table:
            if condition(row):
                vaild_list.append(row)
        return Table(self.table_name +'_filterd',vaild_list)

    def aggregate(self,condition,parameter):
        used_list= []
        for row in self.table:
            if parameter == 'coastline':
                used_list.append(row[parameter])
            else:
                used_list.append(float(row[parameter]))
        result = condition(used_list)
        return result
    def join(self,other_table,common_parameter):
        join_table = []
        for row1 in self.table:
            for row2 in other_table.table:
                if row1[common_parameter] == row2[common_parameter]:
                    merge_row = row1.copy()
                    merge_row.update(row2)
                    join_table.append(merge_row)

        return Table(self.table_name +'_joined_'+other_table.table_name,join_table)
    def __str__(self):
        return self.table_name + ':' + str(self.table)

loader = DataLoader()
cities = loader.load_csv('Cities.csv')
table1 = Table('cities', cities)
countries = loader.load_csv('Countries.csv')
table2 = Table('countries', countries)

my_DB = DB()
my_DB.insert(table1)
my_DB.insert(table2)

my_table1 = my_DB.search('cities')
print("List all cities in Italy:") 
my_table1_filtered = my_table1.filter(lambda x: x['country'] == 'Italy')
print(my_table1_filtered)
print()

print("Average temperature for all cities in Italy:")
print(my_table1_filtered.aggregate(lambda x: sum(x)/len(x), 'temperature'))
print()

my_table2 = my_DB.search('countries')
print("List all non-EU countries:") 
my_table2_filtered = my_table2.filter(lambda x: x['EU'] == 'no')
print(my_table2_filtered)
print()

print("Number of countries that have coastline:")
print(my_table2.filter(lambda x: x['coastline'] == 'yes').aggregate(lambda x: len(x), 'coastline'))
print()

my_table3 = my_table1.join(my_table2, 'country')
print("First 5 entries of the joined table (cities and countries):")
for item in my_table3.table[:5]:
    print(item)
print()

print("Cities whose temperatures are below 5.0 in non-EU countries:")
my_table3_filtered = my_table3.filter(lambda x: x['EU'] == 'no').filter(lambda x: float(x['temperature']) < 5.0)
print(my_table3_filtered.table)
print()

print("The min and max temperatures for cities in EU countries that do not have coastlines")
my_table3_filtered = my_table3.filter(lambda x: x['EU'] == 'yes').filter(lambda x: x['coastline'] == 'no')
print("Min temp:", my_table3_filtered.aggregate(lambda x: min(x), 'temperature'))
print("Max temp:", my_table3_filtered.aggregate(lambda x: max(x), 'temperature'))
print()