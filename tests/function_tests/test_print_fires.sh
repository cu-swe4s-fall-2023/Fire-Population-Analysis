#!/bin/bash
cd ../../src 

test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest

source ssshtest

STOP_ON_FAIL=0


run italy_median_test python print_fires.py --country Italy --country_column 0 --fires_column 2 --file_name ../Agrofood_co2_emission.csv --operation median
assert_in_stdout 7.1188
assert_no_stderr
assert_exit_code 0

# Test when script should exit 
run test_invalid_operation python print_fires.py --country Italy --country_column 0 --fires_column 2 --file_name ../Agrofood_co2_emission.csv --operation invalid
assert_exit_code 2 

# Test using test_data.csv 
run test_fake_data python print_fires.py --country Brazil --country_column 0 --fires_column 2 --file_name ../tests/function_tests/test_data.csv
assert_exit_code 0
assert_in_stdout "Brazil fires: [14.7237, 8.1112, 3.1243, 0.0]"

run test_mean python print_fires.py --country Brazil --country_column 0 --fires_column 2 --file_name ../tests/function_tests/test_data.csv --operation mean
assert_exit_code 0
assert_in_stdout "mean of fires: 6.489799999999999"

run test_nonexistent_country python print_fires.py --country fakecountry --country_column 0 --fires_column 2 --file_name ../tests/function_tests/test_data.csv
# assert_exit_code 1
assert_in_stdout "Country not found: fakecountry"

# Test stddev operation on test_data.csv
run test_stddev python print_fires.py --country Brazil --country_column 0 --fires_column 2 --file_name ../tests/function_tests/test_data.csv --operation stddev
assert_exit_code 0
assert_in_stdout "stddev of fires: [14.7237, 8.1112, 3.1243, 0.0]"

run test_print_operationandcountry python print_fires.py --country Italy --country_column 0 --fires_column 2 --file_name ../Agrofood_co2_emission.csv --operation median
assert_in_stdout "Italy"
assert_in_stdout "median"

run test_exit_code python print_fires.py --country Italy --country_column 0 --fires_column 2 --file_name ../Agrofood_co2_emission.csv --operation invalid
assert_exit_code 2