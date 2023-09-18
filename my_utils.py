# def get_column(file_name, query_column, query_value, result_column=1):
#     results_arr = []
#     with open(file_name, 'r') as file:
#         for line in file: # For each line: split into an array
#             columns = line.strip().split(',')
#             # print("columns: ", columns)
#             # Check to see if the value in query_colum position matches the value stored in query_value
#             query_column_value = columns[query_column] #Get query_column_value
#             if query_column_value == query_value:#if true, add variable from result_column to holding result array
#                 try:
#                     results_value = int(columns[result_column]) # Make sure year is being output as an int
#                     results_arr.append(results_value)
#                 except ValueError:
#                     print('Could not convert year into an int')
#     return results_arr


def get_column(file_name, query_column, query_value, result_column=1):
    results_arr = []
    try:
        with open(file_name, 'r') as file:
            for line in file: # For each line: split into an array
                columns = line.strip().split(',')
                # print("columns: ", columns)
                # Check to see if the value in query_colum position matches the value stored in query_value
                query_column_value = columns[query_column] #Get query_column_value
                if query_column_value == query_value:#if true, add variable from result_column to holding result array
                    try:
                        results_value = int(columns[result_column]) # Make sure year is being output as an int
                        results_arr.append(results_value)
                    except ValueError:
                        print('Could not convert year into an int')
    except FileNotFoundError:
        print(f'Could not find {file_name}.')
    except Exception as e:
        print(f'An unexpected error occurred, error {e}')
    return results_arr
