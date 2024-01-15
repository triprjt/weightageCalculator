from itertools import product
from itertools import combinations_with_replacement
import numpy as np
import os
# import matplotlib.pyplot as plt

# Directory path
directory = "/mnt/data/"


raw_combinations_file = 'All_combinations.txt'
final_combinations_file = 'Final_list.txt'
Input_Data_file = 'Input_Data.txt'
Final_result = 'Final_result.txt'
# Function to write raw combinations to a file


def write_raw_combinations():
    with open(raw_combinations_file, 'w') as file:
        for combination in combinations_with_replacement(range(0, 101, 5), 4):
            file.write(str(combination) + '\n')


write_raw_combinations()


def read_input_data():
    data = []
    with open(Input_Data_file, 'r') as file:
        # Iterate through each line in the file
        for line in file:
            # Split the line into components and convert them to floats
            data_line = [float(x) for x in line.split()]
            # Append the data line to the data list
            data.append(data_line)

    return data


def write_final_combinations(valid_combinations_list):
    with open(final_combinations_file, 'w') as file:
        for item in valid_combinations_list:
            file.write(str(item) + '\n')


# Data provided
data = np.array(read_input_data())
# Extract wavelength and A, B, C, D columns
X = data[:, 0]  # Wavelength
A, B, C, D = data[:, 1], data[:, 2], data[:, 3], data[:, 4]


def valid_combinations():
    for combination in combinations_with_replacement(range(0, 101, 5), 4):
        if sum(combination) == 100:
            yield combination


# Generating valid combinations
valid_combinations_list = list(valid_combinations())
write_final_combinations(valid_combinations_list)


# Function to calculate weighted addition
def calResultSum(p1, p2, p3, p4, i):
    return p1*A[i] + p2*B[i] + p3*C[i] + p4*D[i]


def write_final_result(results):
    with open(Final_result, 'w') as file:
        file.write(
            "(p1, p2, p3, p4)    X          A          B          C          D          E\n")
        for result_tuple in results:
            formatted_result = ' '.join(map(str, result_tuple))
            file.write(formatted_result + '\n')


# Storing results
results = []


def calculate_results():
    for p1, p2, p3, p4 in valid_combinations_list:
        for i in range(0, len(data)):
            x_i = X[i]
            a_i = A[i]
            b_i = B[i]
            c_i = C[i]
            d_i = D[i]
            e_i = calResultSum(p1, p2, p3, p4, i)
            result_tuple = ((p1, p2, p3, p4), x_i, a_i, b_i, c_i, d_i, e_i)
            results.append(result_tuple)

    write_final_result(results=results)


calculate_results()
# Function to filter combinations where the sum is 100
