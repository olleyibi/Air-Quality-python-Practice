
#Calculate the air quality index and display the maximum value
empty = []
def calc_aqi(var1,var2,var3):
  var1 = 100 * (var1/8)
  empty.append(var1)
  var2 = 100 * (var2/20)
  empty.append(var2)
  var3 = 100 * (var3/25)
  empty.append(var3)
  print('\nAQI = ',max(empty))
    


#Gets the values to pass into the above function (aqi)
while True:
  try:
    ozone = int(input('Amount of ozone recorded (parts per hundred million): '))
    assert(ozone > 0), 'Number must be bigger than 0'
    break
  except:
    print("Please enter a nonnegative number")
while True:
  try:
    sulphur = int(input('Amount of sulfur dioxide recorded (parts per hundred million): '))
    assert(sulphur > 0), 'Number must be bigger than 0'
    break
  except:
    print("Please enter a nonnegative number")
while True:
  try:
    particles = int(input('Amount of particles less than 2.5 micrometres diameter recorded (micrograms per cubic metre): '))
    assert(particles > 0), 'Number must be bigger than 0'
    break
  except:
    print("Please enter a nonnegative number")
  

#calls the aqi function to calculate and print the max air quality index)
#AQI_pollutant = 100*(pollutant data reading)/standard

  calc_aqi(ozone,sulphur,particles)

input('\nClick "Enter" to quit.')
