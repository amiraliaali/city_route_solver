import numpy
import pandas
import sys
class RouteFinder:
    def __init__(self, path_to_csv_file):
        self.connections = {}
        self.connections_csv = None
        self.columns = []
        self.path_to_csv_file = path_to_csv_file

    def read_csv(self):
        self.connections_csv = pandas.read_csv(self.path_to_csv_file, sep=";")
        self.columns = self.connections_csv.columns
        if len(self.columns) != 2:
            print("Error: The csv file does not have the correct format. It should have two columns, the first one with the name of the station and the second one with the connections.")
            # exit the program
            sys.exit()
        else:
            print("The csv file has the correct format.")

    def bring_csv_to_dict(self):
        for i in range(len(self.connections_csv)):
            # check if such a station already exists in the dictionary
            if self.connections_csv[self.columns[0]][i] in self.connections:
                # add the connection to the existing station
                self.connections[self.connections_csv[self.columns[0]][i]].add(self.connections_csv[self.columns[1]][i])
            else:
                # create a new station with the connection
                self.connections[self.connections_csv[self.columns[0]][i]] = {self.connections_csv[self.columns[1]][i]}


if "__main__" == __name__:
    route_finder = RouteFinder("connections.csv")
    route_finder.read_csv()
    route_finder.bring_csv_to_dict()
    print(route_finder.connections)

