def get_column(file_name, query_column, query_value, result_column=1):
    """
    Gets data from CSV file

    :param file_name: (str) name of the CSV file
    :param query_column: (int) index of the column in which to search for the query value
    :param query_value: (str) value to search for in the specified query column
    :param result_column: (int) OPTIONAL index of the column where to get data, default 1
    :return: array of ints
    """
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

def find_mean(data):
    """
    Calculates the mean of a list of ints

    :param data: Array of ints
    :return: float: Mean value of the ints in the array
    """
    total = sum(data)
    mean = total/len(data)
    return mean

def find_median(data):
    """
    Calculates the median of an array of integers

    :param data: Array of ints
    :return: float: the median of the integers in the data array
    """
    len_of_data = len(data)
    sort_data = sorted(data) # Sorted function will return the array from smallest -> largest
    find_middle = len_of_data // 2
    if (len_of_data % 2) == 0:
        #if the array has an even len, the median is the average of the middle two elements.
        element_1 = sort_data[find_middle]
        element_2 = sort_data[find_middle - 1]
        median = (element_1 + element_2)/2
    else:
        median = sort_data[find_middle]
    return median

def find_std_dev(data):
    """
    Calculates the standard deviation of an array of integers.
    Find mean, calc squared differences between each data point, calc the avg of the squared differences, take sq root

    :param data: an array of ints
    :return: float: standard deviation of the array
    """
    mean = find_mean(data)
    squared_diff = []
    for i in data:
        deviation = i - mean
        deviation_squared = deviation**2
        squared_diff.append(deviation_squared)

    varince = sum(squared_diff)/len(data)

    std_dev = varince ** 0.5
    return std_dev