import sys
import matplotlib.pyplot as plt
import numpy as np

def load_data(data_file):
    data = np.genfromtxt(data_file, delimiter=',', skip_header=0)  # Since there is no header in the example
    return data

def get_country_name(data_file):
    # Extract the country name from the file name
    file_parts = data_file.split(".")
    if len(file_parts) > 1:
        country_name = file_parts[0]
    else:
        country_name = data_file  # If no extension, use the whole file name

    return country_name

def make_histogram(data, country_name):
    plt.hist(data[:, 1], bins=20, color="skyblue")
    plt.title(f"{country_name} Fire Count Histogram")
    plt.xlabel("Fire Count")
    plt.ylabel("Frequency")

    output_file = f"{country_name}_histogram.png"
    plt.savefig(output_file)
    print(f"Histogram saved as '{output_file}'.")

def make_bar_chart(data, country_name):
    years = data[:, 0].astype(int)
    urban_pop = data[:, 2]
    rural_pop = data[:, 3]

    fig, ax = plt.subplots()
    width = 0.35
    x = np.arange(len(years))
    ax.bar(x - width/2, urban_pop, width, label='Urban Population', color='skyblue')
    ax.bar(x + width/2, rural_pop, width, label='Rural Population', color='lightcoral')

    ax.set_xlabel("Year")
    ax.set_ylabel("Population")
    ax.set_title(f"Urban and Rural Population Bar Chart for {country_name}")
    ax.set_xticks(x)
    ax.set_xticklabels(years, rotation=45, ha='right')
    ax.legend()

    output_file = f"{country_name}_bar_chart.png"
    plt.savefig(output_file)
    print(f"Bar chart saved as '{output_file}'.")

def make_time_series(data, country_name):
    years = data[:, 0].astype(int)  # Convert years to integers
    fire_counts = data[:, 1]

    plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
    plt.plot(years, fire_counts, color='red', marker='o', linestyle='-')
    plt.title(f"Fire Count Time Series for {country_name}")
    plt.xlabel("Year")
    plt.ylabel("Fire Count")
    plt.grid(True)  # Add grid lines for better visualization

    output_file = f"{country_name}_time_series.png"
    plt.tight_layout()  # Ensures that the labels fit within the plot area
    plt.savefig(output_file)
    print(f"Time series scatter plot saved as '{output_file}'.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python hist.py <data_file>")
        sys.exit(1)

    data_file = sys.argv[1]

    data = load_data(data_file)
    country_name = get_country_name(data_file)

    make_histogram(data, country_name)
    make_bar_chart(data, country_name)
    make_time_series(data, country_name)
