import argparse
from my_utils import get_column

# Note to self: see https://docs.python.org/3/library/argparse.html for help with argparse

def main():
    try:
        parser = argparse.ArgumentParser(description='Get fire data for input country')

        parser.add_argument('--country', type=str, help='Name of country')
        parser.add_argument('--country_column', type=int, help='Column index for the country')
        parser.add_argument('--fires_column', type=int, help='Column index for the amount of fires')
        parser.add_argument('--file_name', type=str, help='Name of data file')
        args = parser.parse_args()

        # country='USSR'
        # country_column = 0
        # fires_column = 3
        # file_name = 'Agrofood_co2_emission.csv'
        # fires_USSR = get_column(file_name, country_column, country)
        # fires_USA = get_column(file_name, country_column, 'United States of America')

        fires_country = get_column(file_name=args.file_name, query_column=args.country_column, query_value=args.country)


        # print("USSR Year Fires: ", fires_USSR)
        # print("USA Year Fires: ", fires_USA)

        print(f'Years of {args.country} Fires: {fires_country}')

    except Exception as e:
        print(f'Some unexpected error occurred, error: {e}')

if __name__ == '__main__':
    main()