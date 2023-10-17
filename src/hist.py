import sys
import matplotlib.pyplot as plt
import numpy as np
import my_utils


def load_data(data_file):
    data = np.genfromtxt(data_file, delimiter=',',
                         skip_header=0)  # Since there is no header in the
    # example
    return data


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
    ax.bar(x - width / 2, urban_pop, width, label='Urban Population',
           color='skyblue')
    ax.bar(x + width / 2, rural_pop, width, label='Rural Population',
           color='lightcoral')

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
    if len(sys.argv) != 3:  # Check if there are three command line arguments
        print("Usage: python hist.py <data_file> <str(country_name)>")
        sys.exit(1)

    data_file = sys.argv[1]
    country_name = sys.argv[2]

    data = load_data(data_file)

    make_histogram(data, country_name)
    make_bar_chart(data, country_name)
    make_time_series(data, country_name)

    # Additional statistics using my_utils:
    fire_counts = data[:, 1].astype(int)
    mean_fire_count = my_utils.find_mean(fire_counts)
    median_fire_count = my_utils.find_median(fire_counts)
    std_dev_fire_count = my_utils.find_std_dev(fire_counts)

    print(f"Mean Fire Count: {mean_fire_count}")
    print(f"Median Fire Count: {median_fire_count}")
    print(f"Standard Deviation of Fire Count: {std_dev_fire_count}")
