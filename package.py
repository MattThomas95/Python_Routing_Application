# Mathew Thomas - #001346588
import csv
from hash_table import HashTable

# Insertion of values from CSV file into the hash table
with open('./csv_files/WGUPS_Package_File.csv', encoding='utf-8-sig') as csvfile:
    read_package = csv.reader(csvfile, delimiter=',')

    # Create a new instance of the HashTable class
    hash_table = HashTable()

    # Label each row from CSV file and add to Hash Table
    # Runs on O(n)
    for row in read_package:
        package_id = row[0]
        address = row[1]
        city = row[2]
        state = row[3]
        zipcode = row[4]
        delivery_deadline = row[5]
        mass = row[6]
        notes = row[7]
        if row[7] != "9:05":
            delivery_status = "At Hub"
        if row[7] == "Delayed on flight---will not arrive to depot until 9:05 am":
            delivery_status = "Delayed on Flight"
        delivered_at = "00:00:00"
        truck_number = 0

        package_info = [package_id, address, city, zipcode, delivery_deadline, mass,
                        notes, delivery_status, delivered_at, truck_number, state]

        hash_table.insert(package_id, package_info)


# Reads CSV file and saves address to address_table
# Runs on O(n)
with open('./csv_files/WGUPS_Name_File.csv', encoding='utf-8-sig') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    address_table = []

    for row in readCSV:
        address_table.append(row)

