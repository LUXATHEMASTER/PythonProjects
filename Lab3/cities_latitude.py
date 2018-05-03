from quicksort import *
from city import City


Cities = []  # Create list of City objects

in_file = open("world_cities.txt", "r")  # Open world cities file
for line in in_file:
    s = line.split(",")
    Cities.append(City(s[0], s[1], s[2], int(s[3]), float(s[4]), float(s[5])))  # Add cities to list

in_file.close()



def compare_lat( City1,City2):              #Compare the latitudes of cities
    if City1.latitude <City2.latitude:
        return City1.latitude


sort(Cities,compare_lat)                     #Sort the cities according to latitude

out_file = open("cities_latitude.txt", "w")  # Open another cities file
for i in range(len(Cities)):
    out_file.write(str(Cities[i]))           # Write the ordered cities
    out_file.write('\n')

out_file.close()                             #Close file