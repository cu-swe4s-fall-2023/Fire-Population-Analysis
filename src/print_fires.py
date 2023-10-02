import argparse
# from src.my_utils import *
from my_utils import *

# Note to self: see https://docs.python.org/3/library/argparse.html for help with argparse

def main():
    try:
        parser = argparse.ArgumentParser(description='Get fire data for input country')

        parser.add_argument('--country', type=str, help='Name of country')
        parser.add_argument('--country_column', type=int, help='Column index for the country')
        parser.add_argument('--fires_column', type=int, default=2, help='Column index for the amount of fires')
        parser.add_argument('--file_name', type=str, help='Name of data file')
        parser.add_argument('--operation', type=str, choices=['mean', 'median', 'stddev'], help='Specify the operation to perform (mean, median, stddev)')
        args = parser.parse_args()

        fires_country = get_column(file_name=args.file_name, query_column=args.country_column, query_value=args.country, result_column=args.fires_column)

        if args.operation == 'mean':
            result = find_mean(fires_country)
        elif args.operation == 'median':
            result = find_median(fires_country)
        elif args.operation == 'std_dev':
            result = find_std_dev(fires_country)
        else:
            result = fires_country

        print(f'{args.country} fires: {fires_country}')

        if args.operation:
            print(f'{args.operation} of fires: {result}')

    except Exception as e:
        print(f'Some unexpected error occurred, error: {e}')

if __name__ == '__main__':

    main()
