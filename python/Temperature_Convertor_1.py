print("Welcome to Temperature Convertor Apps")

user_temp = input ("\nEnter temperature in degree Fahrenheit: ")
user_temp = float(user_temp)

temp_Celsius = (5/9)*(user_temp-32.0)
temp_Kelvin = temp_Celsius + 273.0

user_temp = round(user_temp, 2)
temp_Celsius = round(temp_Celsius, 2)
temp_Kelvin = round(temp_Kelvin ,2)

#Displaying Data
print("\nTemperature in degrees Fahrenheit:\t " + str(user_temp))
print("Temperature in degrees Celsius:\t\t " + str(temp_Celsius))
print("Temperature in degrees Kelvin:\t\t " + str(temp_Kelvin))
print("")

