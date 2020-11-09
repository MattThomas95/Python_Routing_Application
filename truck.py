# Mathew Thomas - #001346588

from datetime import datetime, time, date, timedelta
import package

ht = package.hash_table

# Load the trucks with packages
truck1 = [1, 10, 11, 13, 14, 15, 16, 17, 19, 20, 29, 30, 31, 34, 37, 40]
truck2 = [3, 6, 18, 22, 23, 25, 26, 33, 36, 38, 39]
truck3 = [2, 4, 5, 7, 8, 9, 12, 21, 24, 27, 28, 32, 35, 36]

package_route = []  # Initialize package route list

# Gets package ID number from truck and converts to index in distance array
# Runs on O(n)
def parse_truck(truck):
    truck_parsed = []
    index = 0
    while index < len(truck):
        i = ht.lookup(str(truck[index]))[1]
        string_i = str(i)
        indices = [i for i, s in enumerate(package.address_table) if string_i in s]
        indices = indices[0]
        truck_parsed.append(indices)
        index += 1
    return truck_parsed


# Takes the trucks' packages and the path traveled and creates a package route list
# Runs on O(n^2)
def get_packages(truck, path_traveled):
    package_route.clear()
    outer_index = 0
    while outer_index < len(path_traveled):
        while outer_index < len(path_traveled):
            for a in truck:
                b = package.address_table[path_traveled[outer_index]]
                s_b = str(b)
                s_a = (ht.lookup(str(a))[1])
                if s_b.__contains__(s_a):
                    package_route.append(a)
                    truck.remove(a)
            outer_index += 1


# Gets the distance traveled and determines what time each package is delivered
# Hour and minute set what time the truck leaves
# Runs on O(n)
def delivery_time(distance_traveled, pack_route, hour, minute):
    speed = 18 / 60
    a = time(hour, minute, 0)
    i = 0
    while i < len(distance_traveled) - 1:
        distance = float(distance_traveled[i])
        ti = distance / speed
        later = (datetime.combine(date.today(), a) + timedelta(minutes=ti)).time()
        key = str(pack_route[i])
        ht.lookup(key)[8] = str(later)
        a = later
        i += 1


# Get route and add up all distances traveled
# Runs on O(n)
def total_distance(route):
    total = 0
    for ele in range(0, len(route)):
        total += float(route[ele])
    return total
