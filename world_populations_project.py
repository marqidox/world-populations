import pandas as pd
import sqlite3 
conn = sqlite3.connect('db.sqlite')

#In this project, you’ll answer questions using a database of world population by country.

#1. What years are covered by the dataset? (you can manually count the number of years returned).
all_years = pd.read_sql_query('select distinct year from population_years;', conn)

#2. What is the largest population size for Gabon in this dataset?
largest_pop_gabon = pd.read_sql_query('select population from population_years where country is "Gabon" order by population desc limit 1;', conn)

#3. What were the 10 lowest population countries in 2005?
ten_lowest_pop_2005 = pd.read_sql_query('select country from population_years where year is 2005 limit 10;', conn)

#4. What are all the distinct countries with a population of over 100 million in the year 2010?
distinct_con_100mil_2010 = pd.read_sql_query('select distinct country from population_years where population > 1000 and year is 2010', conn)

#5. How many countries in this dataset have the word “Islands” in their name?
con_islands = len(pd.read_sql_query('select distinct country from population_years where country like "%Islands%";', conn))

#6. What is the difference in population between 2000 and 2010 in Indonesia?
dif_pop_2000_to_2010_indonesia = pd.read_sql_query('select max(population) - min(population) from population_years where country is "Indonesia"', conn)

conn.close()
