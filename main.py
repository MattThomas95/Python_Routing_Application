# Mathew Thomas - #001346588

from datetime import time
import package
import shortest_path
import truck

ht = package.hash_table


truck1_parsed = truck.parse_truck(truck.truck1)  # Take the packages on truck1 and return the address
shortest_path.nearest_neighbor(truck1_parsed)  # Find the best route for the truck1 to take
total1 = truck.total_distance(shortest_path.distance_traveled)  # Get total distance traveled for truck1
truck.get_packages(truck.truck1, shortest_path.route)  # Get order that packages were delivered on truck1
pack1 = list(truck.package_route)  # Parse package route to list
truck.delivery_time(shortest_path.distance_traveled, pack1, 8, 0)  # Truck1 leaves at 08:00
shortest_path.reset_lists()  # Clear lists so nearest neighbor can run again


truck2_parsed = truck.parse_truck(truck.truck2)  # Take the packages on truck2 and return the address
shortest_path.nearest_neighbor(truck2_parsed)  # Find the best route for the truck2 to take
total2 = truck.total_distance(shortest_path.distance_traveled)  # Get total distance traveled for truck2
truck.get_packages(truck.truck2, shortest_path.route)  # Get order that packages were delivered on truck2
pack2 = list(truck.package_route)  # Parse package route to list
truck.delivery_time(shortest_path.distance_traveled, pack2, 9, 5)  # Truck2 leaves at 09:05
shortest_path.reset_lists()  # Clear lists so nearest neighbor can run again


truck3_parsed = truck.parse_truck(truck.truck3)  # Take the packages on truck2 and return the address
shortest_path.nearest_neighbor(truck3_parsed)  # Find the best route for the truck2 to take
total3 = truck.total_distance(shortest_path.distance_traveled)  # Get total distance traveled for truck2
truck.get_packages(truck.truck3, shortest_path.route)  # Get order that packages were delivered on truck2
pack3 = list(truck.package_route)  # Parse package route to list
truck.delivery_time(shortest_path.distance_traveled, pack3, 10, 30)  # Truck3 leaves at 10:30 after truck1 returns

sum_totals = total1 + total2 + total3  # Sum of each trucks total distance

print("\nWGUPS ROUTING PROGRAM\n")
print("Route was completed in " + str(sum_totals) + " miles.")


# This gives a prompt for the user
# Determines status of all packages based on time
# Runs on O(log(n))
def user_interface():
    main_menu = input(
        "\n" + """Please select an option below to begin or type 'quit' to quit:
        1. Get status of all packages at the end of the day
        2. Get info for all packages at any time
        """)
    while main_menu != "quit":  # When quit is entered the the application ends
        if main_menu == "1":  # If 1 is entered then all packages are printed
            j = 1
            while j < 41:
                ht.lookup(str(j))[7] = "Delivered"

                # Fixes wrong address
                if ht.lookup(str(j))[6] == "Wrong address listed":
                    ht.lookup(str(j))[1] = "410 S State St"
                    ht.lookup(str(j))[2] = "Salt Lake City"
                    ht.lookup(str(j))[3] = "84111"
                    ht.lookup(str(j))[6] = "Wrong address fixed"

                # Print all package info
                print("Package " + str(ht.lookup(str(j))[0]) + ", " +
                      str(ht.lookup(str(j))[1]) + ", " +
                      str(ht.lookup(str(j))[2]) + ", " +
                      str(ht.lookup(str(j))[10]) + ", " +
                      str(ht.lookup(str(j))[3]) + ", " +
                      str(ht.lookup(str(j))[4]) + ", " +
                      str(ht.lookup(str(j))[5]) + ", " +
                      str(ht.lookup(str(j))[6]) + ", " +
                      str(ht.lookup(str(j))[7]) + ", " +
                      str(ht.lookup(str(j))[8]))
                j += 1
            quit()

        # Lets user enter a time and returns status of all packages at that time
        if main_menu == "2":
            user_input = input("Enter a time (HH:MM) : ")
            (hours, minute) = user_input.split(":")
            hours = int(hours)
            minute = int(minute)

            # Converts user time to a 24 hour time
            if hours == 1:
                hours = 13
            if hours == 2:
                hours = 14
            if hours == 3:
                hours = 15
            if hours == 4:
                hours = 16
            if hours == 5:
                hours = 17
            user_time = time(hours, minute, 0)
            k = 1

            # Determine status of packages at particular time
            while k < 41:
                ht_time = ht.lookup(str(k))[8]
                (hours, minute, seconds) = ht_time.split(":")
                ht_time = time(int(hours), int(minute), int(seconds))
                t1_time = time(8, 0, 0)
                t2_time = time(9, 5, 0)
                t3_time = time(10, 30, 0)
                delay_time = time(9, 5, 0)
                wrong_address_time = time(10, 20, 0)
                # print(ht_time)
                if ht_time >= user_time:
                    # print(str(ht_time) + " " + str(user_time))
                    ht.lookup(str(k))[8] = "00:00:00"
                    ht.lookup(str(k))[7] = "On Truck"
                if user_time <= t1_time:
                    for p in pack1:
                        ht.lookup(str(p))[7] = "At Hub"
                if user_time <= t2_time:
                    for p in pack2:
                        ht.lookup(str(p))[7] = "At Hub"
                if user_time <= t3_time:
                    for p in pack3:
                        ht.lookup(str(p))[7] = "At Hub"
                if ht_time <= user_time:
                    ht.lookup(str(k))[7] = "Delivered"
                k += 1
            m = 1

            # More special cases to account for and a print statement for all packages
            while m < 41:
                if user_time <= delay_time:
                    if ht.lookup(str(m))[6] == "Delayed on flight---will not arrive to depot until 9:05 am":
                        ht.lookup(str(m))[7] = "Delayed on flight"
                if user_time >= wrong_address_time:
                    if ht.lookup(str(m))[6] == "Wrong address listed":
                        ht.lookup(str(m))[1] = "410 S State St"
                        ht.lookup(str(m))[2] = "Salt Lake City"
                        ht.lookup(str(m))[3] = "84111"
                        ht.lookup(str(m))[6] = "Wrong address fixed"
                if ht.lookup(str(m))[7] == "Delivered":
                    print("Package " + str(ht.lookup(str(m))[0]) + ", " +
                          str(ht.lookup(str(m))[1]) + ", " +
                          str(ht.lookup(str(m))[2]) + ", " +
                          str(ht.lookup(str(m))[10]) + ", " +
                          str(ht.lookup(str(m))[3]) + ", " +
                          str(ht.lookup(str(m))[4]) + ", " +
                          str(ht.lookup(str(m))[5]) + ", " +
                          str(ht.lookup(str(m))[6]) + ", " +
                          str(ht.lookup(str(m))[7]) + ", " +
                          str(ht.lookup(str(m))[8]))

                else:
                    print("Package " + str(ht.lookup(str(m))[0]) + ", " +
                          str(ht.lookup(str(m))[1]) + ", " +
                          str(ht.lookup(str(m))[2]) + ", " +
                          str(ht.lookup(str(m))[10]) + ", " +
                          str(ht.lookup(str(m))[3]) + ", " +
                          str(ht.lookup(str(m))[4]) + ", " +
                          str(ht.lookup(str(m))[5]) + ", " +
                          str(ht.lookup(str(m))[6]) + ", " +
                          str(ht.lookup(str(m))[7]))
                m += 1
        quit()

user_interface()
