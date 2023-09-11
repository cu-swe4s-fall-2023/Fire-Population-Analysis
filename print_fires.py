from my_utils import get_column

#get_column(file_name, query_column, query_value, result_column)

country='USSR'
country_column = 0
fires_column = 3
file_name = 'Agrofood_co2_emission.csv'
fires_USSR = get_column(file_name, country_column, country)


fires_USA = get_column(file_name, country_column, 'United States of America')

print("USSR Year Fires: ", fires_USSR)

print("USA Year Fires: ", fires_USA)
