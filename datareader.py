
# importing modules
import csv
import datetime

'''
DataSet class allows easy manipulation of data from .csv files.
'''


class DataSet():

    data_header = []
    data_points = []

    def __init__(self, filename: str, header: bool = False):

        # creates list with contents of specified .csv file
        with open(filename) as file:
            csvfile = csv.reader(file)
            for row in csvfile:
                self.data_points.append(row)

        # if specified, removes headers and places in separate class attribute data_header
        if header:
            self.data_header = self.data_points[0]
            self.data_points.pop(0)

    # converts values in specified columns to float. indices argument is a list of column indices to convert.
    def read_as_float(self, indices: list):
        for n in indices:
            for i in range(len(self.data_points)):
                self.data_points[i][n] = float(self.data_points[i][n])

    # converts values in specified columns to int. indices argument is a list of column indices to convert.
    def read_as_int(self, indices: list):
        for n in indices:
            for i in range(len(self.data_points)):
                self.data_points[i][n] = int(self.data_points[i][n])

    # converts values in specified columns to standard datetime strings. use must define the input date format.
    def read_as_date(self, indices: list, d_format: str):

        time_type_list = ['Y', 'M', 'D', 'h', 'm']
        index_list = []
        count_list = []

        for i in range(0, len(time_type_list)):
            index_list.append(d_format.find(time_type_list[i]))
            count_list.append(d_format.count(time_type_list[i]))

        for n in range(0, len(indices)):
            for a in range(0, len(self.data_points)):
                time_list = []
                for i in range(0,len(time_type_list)):
                    time_list.append(int(self.data_points[a][indices[n]][index_list[i]:index_list[i]+count_list[i]]))
                self.data_points[a][indices[n]] = str(datetime.datetime(*time_list))


# extracts a column from a DataSet in list format
def make_vector(data: DataSet, column: int, statistics: bool=False):

    vector = []
    for i in data.data_points:
        vector.append(i[column])

    for i in vector:
        try:
            float(i)
        except ValueError:
            print('WARNING: Vector contains non-numerical values.')
    if statistics:
        return vector, [len(vector), max(vector), min(vector), sum(vector) / len(vector)]
    else:
        return vector
  
