#!/bin/bash

# Three examples of running print_fires.py; one that works and two that gives errors
# One that works:
#python print_fires.py --country Italy --country_column 0 --fires_column 1 --file_name ../Agrofood_co2_emission.csv
# Two that gives errors:
#python print_fires.py --country USSR --country_column 0 --fires_column 3 ../Agrofood_c02.csv
#python print_fires.py --country United States of America --country_column 0 --fires_column 3 --file_name ../Agrofood_co2_emission.csv

python print_fires.py --country Italy --country_column 0 --fires_column 2 --file_name ../Agrofood_co2_emission.csv --operation median
python print_fires.py --country Italy --country_column 0 --file_name ../Agrofood_co2_emission.csv

# I had to add this command because my terminal kept closing before I could read it:
read -p "Press Enter to close this terminal"
