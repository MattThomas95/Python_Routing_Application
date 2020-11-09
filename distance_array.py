# Mathew Thomas - #001346588

import csv

# This class creates a 2D array to store the distances between points.
class DistanceArray:

    # Creates an empty 27 x 27 array
    def __init__(self):
        w, h = 27, 27
        self.distance_table = [[0 for x in range(w)] for y in range(h)]

    # Adds value to specific row and column
    def add_cell(self, row, col, value):
        self.distance_table[row][col] = value

    # Returns entire 2D array
    def get_distance_table(self):
        print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                         for row in self.distance_table]))

    # Returns value at specific row and column
    def get_value(self, row, column):
        return self.distance_table[row][column]

    # Returns all values in a column
    def get_column(self, column):
        return self.distance_table[column]


# Add all distances from CSV File to the 2D array
# Runs on O(1)
def add_all_distances(dist_array):
    with open('./csv_files/WGUPS_Distance_File.csv', encoding='utf-8-sig') as csvfile:
        read_distance = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC, delimiter=',')
        data = list(read_distance)
        a = dist_array

        row = 0
        column = 0
        i = 0
        j = 0
        while j < 27:
            while i < 27:
                a.add_cell(row, column, data[row][column])
                column += 1
                i += 1
            row += 1
            j += 1
            column = 0
            i = 0


