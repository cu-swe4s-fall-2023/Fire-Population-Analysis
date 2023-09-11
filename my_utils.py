def get_column(file_name, query_column, query_value, result_column):
    results_arr = []
    with open(file_name, 'r') as file:
        for line in file: # For each line: split into an array
            columns = line.strip().split(',')
            # Check to see if the value in query_colum position matches the value stored in query_value
            query_column_value = columns[query_column] #Get query_column_value
            if query_column_value == query_value:#if true, add variable from result_column to holding result array
                results_arr.append(columns[results_column])
    return results_arr
