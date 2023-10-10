# Best Practices 

[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/oQi7O4AA)

This repo contains the python project for brief data analysis of fires by country/year.

Uses repo from assignment-2 (python refresher).

## Table of Contents
- [Documentation](#documentation-a-namedocumentationa)
  - [`my_utils.py`](#myutilspy-a-namemy-utilsa)
  - [`print_fires.py`](#printfirespy-a-nameprint-firesa)
  - [`run.sh`](#runsh-a-namerunsha)
- [Usage](#usage-a-nameusagea)
- [Updates](#updates-a-nameupdatesa)
  - [V 1.0](#v-10-a-namev-1a)
  - [V 2.0](#v-20-a-namev-2a-)
  - [V 3.0](#v-30-a-namev-3a)
  - [V 3.1](#v-31-a-namev-31a)
  - [V 4.0](#v-40-a-namev-4a)
- [License](#license)

## Documentation <a name="documentation"></a>

### `my_utils.py` <a name="my-utils"></a>


#### `get_column(file_name, query_column, query_value, result_column=1)`
- Opens a CSV file containing data delimited by commas.
- Returns an array of values based on inputs.
- Default output is a list of years that fires occurred (as integers).
- Parameters:
    - `file_name` (str): Name of the CSV file containing data.
    - `query_column` (int): Column index for the query condition.
    - `query_value` (str): Value used to find a match in the query column (e.g., country name).
    - `result_column` (int, optional): Column index for the result. Default is 1, representing the year when the fire occurred for the specified country.
- Raises a `ValueError` if the array is empty or if the specified result column does not exist.

#### `find_mean(data)`
- Calculates the mean of a list of integers.
- Parameters:
    - `data` (list): Array of integers.
- Returns:
    - `float`: Mean value of the integers in the array.
- Raises a `ValueError` if the array is empty.

#### `find_median(data)`
- Calculates the median of an array of integers.
- Parameters:
    - `data` (list): Array of integers.
- Returns:
    - `float`: The median of the integers in the data array, or `None` if the array is empty.

#### `find_std_dev(data)`
- Calculates the standard deviation of an array of integers.
- Parameters:
    - `data` (list): An array of integers.
- Returns:
    - `float`: Standard deviation of the array.
- Raises a `ValueError` if the array is empty.


### `print_fires.py` <a name="print-fires"></a>
This script will do brief analysis on fires by input country.

#### Command-line argparse
Allows user to input parameters via command line.
- `--country` (str): Specifies the name of the country to query.
- `--country_column` (int): Specifies the column index for the country in the CSV file.
- `--fires_column` (int): Specifies the column index for the amount of fires in the CSV file
- `--file_name` (str): Specifies the name of the data file in CSV format.
- `--operation` (str): Specifies the statistics operation to perform (e.g., "mean", "median", "stddev").

### `run.sh` <a name="runsh"></a>
~~This shell script includes 3 examples for running `print_fires.py`, as required by the assignment.~~
<br>
With the 3.0 release, `run.sh` will now contain two examples of how `print_fires.py` could be used.

#### Example that works:

```shell
python print_fires.py --country Italy --country_column 0 --fires_column 1 --file_name ../Agrofood_co2_emission.csv
```

#### Examples that give errors:
```shell
python print_fires.py --country USSR --country_column 0 --fires_column 3 ../Agrofood_c02.csv
python print_fires.py --country "United States of America" --country_column 0 --fires_column 3 --file_name ../Agrofood_co2_emission.csv
```


## Updates <a name="updates"></a>

### V 4.0 <a name="v-4"></a>
- Implemented automated testing on branch push and pull requests on main branch.

### V 3.1 <a name="v-3.1"></a>
- Added documentation on how to run tests.

### V 3.0 <a name="v-3"></a>
- Added some basic statistics functions to `my_utils.py`
- Added additional functionality to `print_fires.py` for statistics functions.
  - Added `--operation` argparse (optional) to call statistics functionality on data.
- Added unit tests and function tests using `ssshtest`
  - See https://github.com/ryanlayer/ssshtest for info about `ssshtest` and dependencies

### V 2.0 <a name="v-2"></a> 
- Added `main()` function in `print_fires.py`
- Added argsparse functionality to `print_fires.py`
- Updated `my_utils.py` to return the output array containing ints
- Now catches errors and exceptions with `file_name` arguments and when converting values to ints

### V 1.0 <a name="v-1"></a>
- Improved `get_column()` Function
  - `result_column` now defaults to 1 if not specified, which will print the year of fires.
- Added a shell script runs `print_fires.py` via Python.


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