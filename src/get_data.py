import sys

print(sys.argv)

def generate_output_filename(country_name):
    return f"{country_name}.txt"

def extract_country_data(file_name, country_name):
    """
    Copy data for a specified country from the file and save it to a txt file.

    :param file_name: Name of the CSV file.
    :param country_name: Name of the country.
    """
    out_file = generate_output_filename(country_name)
    try:
        found = False
        with open(out_file, 'w') as output_file:
            with open(file_name, 'r') as input_file:
                header = next(input_file)  # Skips the header
                for line in input_file:
                    columns = line.strip().split(',')
                    if len(columns) >= 27: 
                        data_country_name = columns[0]
                        year = columns[1]
                        fires = columns[2]
                        forest_fires = columns[3]
                        urban_pop = columns[26]
                        rural_pop = columns[25]

                        if data_country_name == country_name:
                            if fires and forest_fires and urban_pop and rural_pop:  # makes sure we dont grab empty fields
                                found = True
                                total_fires = float(fires) + float(forest_fires)
                                years = int(year)
                                urban_population = float(urban_pop)
                                rural_population = float(rural_pop)
                                output_file.write(f"{year},{total_fires},{urban_population},{rural_population}\n")

        if not found:
            raise ValueError(f"Country '{country_name}' not found in the CSV file.")

        print(f"Data for '{country_name}' saved to '{out_file}'.")
    except FileNotFoundError:
        print(f"Data file '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python get_data.py <datafile.csv> <country name>")
        sys.exit(1)

    data_file = sys.argv[1]
    country = sys.argv[2]

    extract_country_data(data_file, country)


# import sys

# file_name = sys.argv[1]
# country_name = sys.argv[2]
# out_file = sys.argv[3]


# f = open(out_file, 'w')
# for l in open(file_name):
#     A = l.rstrip().split(',')
#     if A[0] == country_name:
#         f.write(str(float(A[2]) + float(A[3])) + '\n')