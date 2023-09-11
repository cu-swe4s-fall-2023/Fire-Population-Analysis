[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/oQi7O4AA)
# python-refresher

## Updated `my_utils.py`
- `get_column()` function : opens csv file delimited by commas, returns array of values based on input criteria.

## Updated `print_fires.py`
- Improved get_colum() function : `result_column` now defaults to 1 if nothing is specified, this will print the year of the fires.
- fixed typo with results column

## Created `run.sh`
- shell script runs `print_fires.py` via python. 
- (Make sure `run.sh` is executable with `$ chmod +x run.sh`
- run by making sure `print_fires.py` is in the same directory as `run.sh`, and execute with `$./run.sh`