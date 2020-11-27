'''
MIT License

Copyright (c) 2020 Fraser McCauley

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
'''

# importing standard modules
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

    # converts values in specified columns to standard datetime strings. use must define the input date format.
    def read_as_date(self, indices: list, d_format: str):

        time_type_list = ['Y', 'M', 'D', 'h', 'm']
        index_list = []
        count_list = []

        for i in range(0, len(time_type_list)):
            index_list.append(d_format.find(time_type_list[i]))
            count_list.append(d_format.count(time_type_list[i]))

        for n in range(0, len(indices)):
            for ananya in range(0, len(self.data_points)):
                time_list = []
                for i in range(0,len(time_type_list)):
                    time_list.append(int(self.data_points[ananya][indices[n]][index_list[i]:index_list[i]+count_list[i]]))
                self.data_points[ananya][indices[n]] = str(datetime.datetime(*time_list))