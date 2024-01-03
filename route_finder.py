import numpy
import pandas
import sys
class RouteFinder:
    def __init__(self, path_to_csv_file):
        self.connections = {}
        self.connections_csv = None
        self.columns = []
        self.path_to_csv_file = path_to_csv_file
        self.read_csv()
        self.bring_csv_to_dict()
        self.shortest_path = []
        self.already_visited = []

    def read_csv(self):
        self.connections_csv = pandas.read_csv(self.path_to_csv_file, sep=";")
        self.columns = self.connections_csv.columns
        if len(self.columns) != 2:
            print("Error: The csv file does not have the correct format. It should have two columns, the first one with the name of the station and the second one with the connections.")
            # exit the program
            sys.exit()
        else:
            print("Read csv file successfully.")

    def bring_csv_to_dict(self):
        for i in range(len(self.connections_csv)):
            # check if such a station already exists in the dictionary
            if self.connections_csv[self.columns[0]][i] in self.connections:
                # add the connection to the existing station
                self.connections[self.connections_csv[self.columns[0]][i]].append(self.connections_csv[self.columns[1]][i])
            else:
                # create a new station with the connection
                self.connections[self.connections_csv[self.columns[0]][i]] = [self.connections_csv[self.columns[1]][i]]

    def find_route(self, start_station, end_station):
        if start_station not in self.connections:
            return
        
        self.shortest_path.append(start_station)

        if start_station == end_station:
            return
        else:
            for i in range(len(self.connections[start_station])):
                if self.connections[start_station][i] not in self.already_visited:
                    self.already_visited.append(self.connections[start_station][i])
                    self.find_route(self.connections[start_station][i], end_station)
                    return self.shortest_path
                else:
                    self.shortest_path.pop()







if "__main__" == __name__:
    route_finder = RouteFinder("connections.csv")
    # starting_station = input("Please enter the starting station: ")
    # ending_station = input("Please enter the ending station: ")
    starting_station = "berlin"
    ending_station = "dubai"
    route_finder.find_route(starting_station, ending_station)
    route = route_finder.shortest_path
    if route == []:
        print("There is no route between the two stations.")
    else:
        print("The shortest route is: ")
        for i in range(len(route)):
            print(route[i], end="")
            if i != len(route) - 1:
                print(" -> ", end="")
        print()
