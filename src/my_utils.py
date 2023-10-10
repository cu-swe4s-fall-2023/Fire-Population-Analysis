def get_column(file_name, query_column, query_value, result_column=3):
    """
    Gets data from CSV file

    :param file_name: (str) name of the CSV file
    :param query_column: (int) index of the column in which to search for the
    query value
    :param query_value: (str) value to search for in the specified query column
    :param result_column: (int) OPTIONAL index of the column where to get
    data, default 3
    :return: array of ints
    """
    results_arr = []
    try:
        with open(file_name, 'r') as file:
            for line in file:  # For each line: split into an array
                columns = line.strip().split(',')
                if len(columns) > result_column:  # check if the specified
                    # result_column exists
                    # Check to see if the value in query_column position
                    # matches the value stored in query_value
                    query_column_value = columns[
                        query_column]  # Get query_column_value
                    if query_column_value == query_value:
                        try:
                            results_value = float(
                                columns[
                                    result_column])  # Make sure year is
                            # being output as not a string
                            results_arr.append(results_value)
                        except ValueError:
                            print(
                                f'Could not convert column {result_column} '
                                f'value into an int')
                else:
                    print(
                        f'Result column {result_column} does not exist in '
                        f'line: {line}')

        if not results_arr:
            raise ValueError('Cannot find mean of an empty array')
    except FileNotFoundError:
        print(f'Could not find {file_name}.')
        raise
    except Exception as e:
        print(f'An unexpected error occurred, error {e}')
    return results_arr


def find_mean(data):
    """
    Calculates the mean of a list of ints

    :param data: Array of ints
    :return: float: Mean value of the ints in the array
    """
    if len(data) == 0:
        raise ValueError('Cannot find mean of an empty array')
    total = sum(data)
    mean = total / len(data)
    return mean


def find_median(data):
    """
    Calculates the median of an array of integers

    :param data: Array of ints
    :return: float: the median of the integers in the data array
    """
    len_of_data = len(data)
    if len_of_data == 0:
        return None

    sort_data = sorted(
        data)  # Sorted function will return the array from smallest -> largest
    find_middle = len_of_data // 2
    if (len_of_data % 2) == 0:
        # if the array has an even len, the median is the average of the
        # middle two elements.
        element_1 = sort_data[find_middle]
        element_2 = sort_data[find_middle - 1]
        median = (element_1 + element_2) / 2
    else:
        median = sort_data[find_middle]
    return median


def find_std_dev(data):
    """
    Calculates the standard deviation of an array of integers.
    Find mean, calc squared differences between each data point, calc the avg
    of the squared differences, take sq root

    :param data: an array of ints
    :return: float: standard deviation of the array
    """
    if len(data) == 0:
        raise ValueError('Cannot find std dev of an empty array')

    mean = find_mean(data)
    squared_diff = []
    for i in data:
        deviation = i - mean
        deviation_squared = deviation ** 2
        squared_diff.append(deviation_squared)

    varince = sum(squared_diff) / len(data)

    std_dev = varince ** 0.5
    return std_dev
