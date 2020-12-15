#Welcome Message
print("Welcome to Speed Conversion App")
print("This will convert speed from miles-per-hour to meter-per-second")

#Taking Data from User
print("\n")
speed_user = input("What is your speed in miles pre hour? : ")
speed_user = float(speed_user)
print("You entered speed: " + str(speed_user))

speed_user_new = speed_user / 2.237
speed_user_new = round(speed_user_new, 2)
print("Your speed in meters-per-second is: " + str(speed_user_new))