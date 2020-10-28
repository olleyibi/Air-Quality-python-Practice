#OLLEY IBIDAMOLA
#2200216600

# this function opens filename and return its content in form dictionary
def read_data(filename):
  keys = []
  values = []
  dict1 = {}
  with open(filename,'r') as file:
    for line in file:
      key, value = line.strip().split(',')
      keys.append(key)
      values.append(float(value))
    for i in range(len(keys)):
      if keys[i] not in dict1:
        dict1[keys[i]] = [values[i]]
      else:
        for j in dict1:
          if j == keys[i]:
            dict1[j].append(values[i])
    return dict1
    #pass  # TODO: Implement this correctly

# function to get the average figure of values contained in each dictionary key on the dictionary
def get_average_dictionary(readings):
  dict2 = {}
  for i in readings:
    j = sum(readings[i])/len(readings[i])
    dict2[i] = j
  return dict2
    #pass  # TODO: Implement this correctly

FILENAME = "readings.txt"

if __name__ == "__main__":
    try:
        readings = read_data(FILENAME)
        averages = get_average_dictionary(readings)

        # Loops through the keys in averages, sorted from that with the largest associated value in averages to the lowest - see https://docs.python.org/3.5/library/functions.html#sorted for details
        for location in sorted(averages, key = averages.get, reverse = True):
            print(location, averages[location])

    except (IOError, ValueError):
        print("Error reading {}".format(FILENAME))
        print("Please ensure the file exists and matches the required format")
        print("(each line should begin with a location name, followed by a comma, followed by an AQI reading)")
