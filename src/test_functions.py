from my_utils import *

# get_column(file_name, query_column, query_value, result_column):
file_name = '../Agrofood_co2_emission.csv'
q_col = 2
q_value = 'example'
result_col = 3

result = get_column(file_name, q_col, q_value, result_col)

print(result)