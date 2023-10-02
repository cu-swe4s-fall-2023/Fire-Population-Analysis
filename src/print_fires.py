import argparse
# from src.my_utils import *
from my_utils import *

# Note to self: see https://docs.python.org/3/library/argparse.html for help with argparse

def main():
    try:
        parser = argparse.ArgumentParser(description='Get fire data for input country')

        parser.add_argument('--country', type=str, help='Name of country')
        parser.add_argument('--country_column', type=int, help='Column index for the country')
        parser.add_argument('--fires_column', type=int, help='Column index for the amount of fires')
        parser.add_argument('--file_name', type=str, help='Name of data file')
        args = parser.parse_args()

        fires_country = get_column(file_name=args.file_name, query_column=args.country_column, query_value=args.country)

        # testing new statistics functions:
        mean_fires = find_mean(fires_country)
        median_fires = find_median(fires_country)
        std_dev_fires = find_std_dev(fires_country)


        print(f'Years of {args.country} Fires: {fires_country}')
        print(f'Mean fires: {mean_fires}')
        print(f'Median fires: {median_fires}')
        print(f'Std deviation of fires: {std_dev_fires}')

    except Exception as e:
        print(f'Some unexpected error occurred, error: {e}')

if __name__ == '__main__':

    main()
