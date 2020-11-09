# Mathew Thomas - #001346588

import distance_array

a = distance_array.DistanceArray()  # Initialize DistanceArray()
distance_array.add_all_distances(a)  # Add all distances to array

# Create lists
distance_traveled = []
distance_list = []
route = [0]  # route starts at hub which is index[0] in array

# Nearest Neighbor algorithm is used to find best route for each truck
# Every truck starts at the hub which is index[0][0] in the 2D distance array
# The algorithm finds the address closest to the hub, from all packages on the truck
# That address is then popped from the truck and the algorithm
# Then searches from current address and finds the next nearest address
# This is repeated until all addresses have been visited and the truck heads back to hub
# Runs on O(n^2)
def nearest_neighbor(package_index_list):

    # Initialize values
    i = 0
    next_search = 0
    pack_list = package_index_list

    # The first while loop runs until the truck is empty
    while len(pack_list) > 0:

        # The second while loop gets the current row
        while i < len(pack_list):
            index = pack_list[i]
            j = a.distance_table[next_search][index]
            distance_list.append(j)
            i += 1

        min_distance = str(min(distance_list))  # Find the smallest distance in row
        distance_traveled.append(min_distance)  # Append smallest distance to list
        di = distance_list.index(min(distance_list))  # Find the index of min distance
        next_search = pack_list[di]  # Set nearest distance to be searched next
        distance_list.clear()  # Clear list

        # This determines if only one package is left and sends it back to hub
        if len(pack_list) == 1:
            route.append(pack_list[0])
            ti = a.distance_table[0][pack_list[0]]
            distance_traveled.append(ti)
            pack_list.pop(0)
            route.append(0)
        else:
            route.append(next_search)
            pack_list.pop(di)
            i = 0

    return route  # Returns the sorted route


# Reset lists so the algorithm can be run again with new values
def reset_lists():
    distance_list.clear()
    distance_traveled.clear()
    route.clear()
    route.append(0)
