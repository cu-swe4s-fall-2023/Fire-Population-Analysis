# SWE4S Best Practices 

This repo contains the python project for brief data analysis of fires by country/year.

Uses repo from assignment-2 (python refresher).

## Table of Contents


## Introduction 
This project focuses on the analysis of fires by country and year. The dataset includes information on the occurrence of fires in different countries over time. The analysis aims to provide insights into fire patterns and their relationship to factors such as urban and rural population.

## Results 
Analysis on the Italy dataset produced three key figures:

1. Fire Count Histogram: This histogram visualizes the distribution of fire counts across different years, providing an overview of fire occurrences over time.
   
<img src="/docs/figures/Italy_histogram.png" width="50%">

2. Urban and Rural Population Bar Chart: This bar chart shows the urban and rural population for each year. It helps identify trends and potential correlations between population changes and fire occurrences.

<img src="/docs/figures/Italy_bar_chart.png" width="50%"/>

3. Fire Count Time Series Plot: This time series plot tracks the fire counts over the years, allowing for the observation of patterns and trends in fire occurrences.

<img src="/docs/figures/Italy_time_series.png" width="50%"/>

- Our brief analysis also showed some brief statistics:
<br>
<img src="/docs/figures/fire_stats.png" width="50%"/>

### Methods
- **Data Retrieval**: We retrieved the dataset, `Argrofood_co2_emission.csv`, from a publicly accessible Google Drive link using `wget`:

```commandline
$ wget -O Argrofood_co2_emission.csv 'https://docs.google.com/uc?export=download&id=1Wytf3ryf9EtOwaloms8HEzLG0yjtRqxr'
```

- **Data Processing**: We processed the dataset using `get_data.py` to copy and save relevant data for Italy to a txt file:
```commandline
$ python get_data.py Argrofood_co2_emission.csv Italy
```

- **Data Visualization**: We created the three figures from the new dataset with `hist.py`:
```commandline
$ python hist.py Italy.txt Italy
```

- To generate the figures displayed in this README, simply run snakemake from ../src:

```commandline
$ snakemake -c1
```

## Documentation 

### `my_utils.py` 
Collection of utilities used for data analysis, including mean, median, and std deviation.

### `print_fires.py` 
This script performs a brief analysis on fires by input country. It provides command-line argparse for user input. 

<details>
<summary> Command-line argparse </summary>

Allows user to input parameters via command line.
- `--country` (str): Specifies the name of the country to query.
- `--country_column` (int): Specifies the column index for the country in the CSV file.
- `--fires_column` (int): Specifies the column index for the amount of fires in the CSV file
- `--file_name` (str): Specifies the name of the data file in CSV format.
- `--operation` (str): Specifies the statistics operation to perform (e.g., "mean", "median", "stddev").
</details>

#### Example command:

```shell
python print_fires.py --country Italy --country_column 0 --fires_column 1 --file_name ../Agrofood_co2_emission.csv
```

### `run.sh` 
A shell script for running `print_fires.py` with examples included. 



### `get_data.py`
A script to extract and process data from a CSV file and save it to a text file.

### `hist.py`

A script for generating histograms, bar charts, and time series plots, along
with calculating statistics from data.

## Updates

<details>
<summary>Expand for version release updates</summary>

### V 5.0

- Added snakemake workflow to project.
- Added `hist.py` and `get_data.py` to create figures from csv data.
- Added scientific findings and methodology to README.

### V 4.1

- Patched `.test.yml` to check for PEP8 style using pycodestyle action.

### V 4.0

- Implemented automated testing on branch push and pull requests on main
  branch.

### V 3.1

- Added documentation on how to run tests.

### V 3.0 
- Added some basic statistics functions to `my_utils.py`
- Added additional functionality to `print_fires.py` for statistics functions.
  - Added `--operation` argparse (optional) to call statistics functionality on data.
- Added unit tests and function tests using `ssshtest`
  - See https://github.com/ryanlayer/ssshtest for info about `ssshtest` and dependencies

### V 2.0 
- Added `main()` function in `print_fires.py`
- Added argsparse functionality to `print_fires.py`
- Updated `my_utils.py` to return the output array containing ints
- Now catches errors and exceptions with `file_name` arguments and when converting values to ints

### V 1.0 
- Improved `get_column()` Function
  - `result_column` now defaults to 1 if not specified, which will print the year of fires.
- Added a shell script runs `print_fires.py` via Python.
</details>

## Usage <a name="usage"></a>
- Start from clone
- Run from main project directory, execute with `$ ./run.sh`.
- Example of how to run `print_fires.py` with argparse:

```shell
$ python print_fires.py --country Italy --country_column 0 --fires_column 1 --file_name Agrofood_co2_emission.csv
```

- Run unit tests from ../tests/unit_tests/ with:

```shell 
$ python test_my_utils.py
```

- Run function tests from ../tests/function_tests/ 
- For example: 

```shell
$ ./test_print_fires.sh
```

## LICENSE

MIT License

Copyright (c) 2023 cu-swe4s-fall-2023

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
