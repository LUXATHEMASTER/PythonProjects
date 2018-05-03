from city import City
Cities = []  # Create  a list of City objects

in_file = open("world_cities.txt", "r")  # Open world cities file
for line in in_file:
    s = line.split(",")
    Cities.append(City(s[0], s[1], s[2], int(s[3]), float(s[4]), float(s[5])))  # Add cities to list

in_file.close()         #Close file

out_file = open("cities_out.txt", "w")  # Open another cities files
for i in range(len(Cities)):
    out_file.write(str(Cities[i]))  # Write the orderd cities
    out_file.write('\n')

out_file.close()        #Close file
