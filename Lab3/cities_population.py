from quicksort import *
from city import City


Cities = []                              # Create list of City objects

in_file = open("world_cities.txt", "r")  # Open world cities file
for line in in_file:
    s = line.split(",")
    Cities.append(City(s[0], s[1], s[2], int(s[3]), float(s[4]), float(s[5])))  # Add Cities to list from file

in_file.close()



def compare_pop( City1,City2):            #Compare population of two Cities
    if City1.pop >=City2.pop:
        return City1.pop


sort(Cities,compare_pop)  #Sort Cities

out_file = open("cities_population.txt", "w")  # Open another cities files
for i in range(len(Cities)):
    out_file.write(str(Cities[i]))             # Write the ordered cities
    out_file.write('\n')

out_file.close()                               #Close the file