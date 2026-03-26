import sys

print("\nWELCOME TO THE TRAFFIC SPEED CHECKER! PLEASE FOLLOW THE STEPS BELOW.")

roadType = input("\nenter the road type (city/school/higway): ").lower() # the type of road the user was driving on & allows for variaton as long as the letters are the same

if roadType not in ["city", "school", "highway"]:
    print("this is not a valid road type. please RESTART and enter a road type from the provided options")
    sys.exit()
# the speed the user is going and the message provided if there is an invalid input
speed = int(input("\nenter your speed (AS A NUMBER): ")) 
if speed < 0:
    print("this is not a valid speed. please RESTART and enter a speed greater than 0 OR enter the speed as a numerical value")
    sys.exit()

# the number of previous offenses and the message provided if there is an invalid input
prevOffenses = int(input("\nenter your number of previous offenses: ")) 
if prevOffenses < 0:
    print("this is not a valid numer of previous offenses. please RESTART and enter a number greater or equal to 0 ")
    sys.exit()

fine = 0 # the price the user has to pay
violation = "" # the severity of the violation (minor/major./severe)
incurrences = "" # the incurrences that come with the violation (license suspension & warning / community service )
speedLimit = 0 # the speed limit for each road type

# checks to make sure that the user inputs a valid road type, and suggests re-trying if not.


# checks the roadtype, speed, and number of previous occurences and provides the consequences
if "city" in roadType and (speed <=50):
    violation = "NONE"
    incurrences = "NONE"
    speedLimit = 50
    print("\nYOU ARE GOING THE SPEED LIMIT! THERE IS NO FINE")
elif "city" in roadType and (speed >= 51 and speed <= 71):
    fine = 1000
    violation = "MINOR"
    incurrences = "NONE"
    speedLimit = 50
    if prevOffenses >= 2:
        fine = (fine * 1.5)
    print("\nMINOR VIOLATION:", "YOU OWE", fine,"RUPEES")
elif "city" in roadType and (speed >=71 and speed <= 100):
    fine = 2500
    violation = "MAJOR"
    incurrences = "NONE"
    speedLimit = 50
    if prevOffenses >= 2:
        fine = (fine * 1.5)
    print("\nMAJOR VIOLATION: YOU OWE", fine,"RUPEES")
elif "city" in roadType and (speed > 100):
    fine = 5000
    violation = "SEVERE"
    incurrences = "LICENSE WARNING"
    speedLimit = 50
    if prevOffenses >= 2:
        fine = (fine * 1.5)
    print("\nSEVERE VIOLATION: YOU OWE", fine,"RUPEES AND NOW HAVE INCURRED A LICENSE WARNING")
elif "school" in roadType and (speed <=30):
    violation = "NONE"
    incurrences = "NONE"
    speedLimit = 30
    print("\nYOU ARE GOING THE SPEED LIMIT! THERE IS NO FINE")
elif "school" in roadType and (speed >= 31 and speed <= 50):
    fine = 2000
    violation = "MINOR"
    incurrences = "NONE"
    speedLimit = 30
    if prevOffenses >= 2:
        fine = (fine * 1.5)
    print("\nMINOR VIOLATION: YOU OWE", fine,"RUPEES")
elif "school" in roadType and (speed > 50):
    fine = 5000
    violation = "MAJOR"
    incurrences = "COMMUNITY SERVICE"
    speedLimit = 30
    if prevOffenses >= 2:
        fine = (fine * 1.5)
    print("\nMAJOR VIOLATION: YOU OWE", fine,"RUPEES AND HAVE INCURRED COMMUNITY SERVICE")
elif "highway" in roadType and (speed <=80):
    violation = "NONE"
    incurrences = "NONE"
    speedLimit = 80
    print("\nYOU ARE GOING THE SPEED LIMIT! THERE IS NO FINE")
elif "highway" in roadType and (speed >= 81 and speed <= 100):
    fine = 1500
    violation = "MINOR"
    incurrences = "NONE"
    speedLimit = 80
    if prevOffenses >= 2:
        fine = (fine * 1.5)
    print("\nMINOR VIOLATION: YOU OWE", fine,"RUPEES")
elif "highway" in roadType and (speed >=101 and speed <= 130):
    fine = 3500
    violation = "MAJOR"
    incurrences = "NONE"
    speedLimit = 80
    if prevOffenses >= 2:
        fine = (fine * 1.5)
    print("\nMAJOR VIOLATION: YOU OWE", fine,"RUPEES")
elif "highway" in roadType and (speed > 130):
    fine = 7000
    violation = "SEVERE"
    incurrences = "LICENSE SUSPENSION"
    speedLimit = 80
    if prevOffenses >= 2:
        fine = (fine * 1.5)
    print("\nSEVERE VIOLATION: YOU OWE", fine,"RUPEES AND NOW HAVE INCURRED A LICENSE SUSPENSION")
else:
    print("\ninvalid road type")

overUnder = "" # recognizes if the user want over or under the speed limit for the traffic report
difference = "" # calculates how much the user is over or under the speed limit

# asks the user if they want a final report; creates one if yes, and thanks the user if not.
report = input("\nWOULD YOU LIKE A FINAL REPORT? (yes or no) ").lower()
if "yes" in report:
    if (speed > speedLimit): # if the speed is greater than the limit, the user is going over and that can be translated accurately in the report.
            difference =  (speed - speedLimit)
            overUnder = "OVER"
    else: # if the speed limit is greater than the speed, the user is going under and that can be translated accurately in the report.
            difference =  (speedLimit - speed)
            overUnder = "UNDER"
    print("FINE:", fine, "RUPEES  // VIOLATION:", violation, "// ROAD TYPE:", roadType.upper(), "// INCURRENCES:", incurrences, "// PREVIOUS OFFENSES:", prevOffenses, "\n*THE SPEED LIMIT WAS", speedLimit, "KM/H AND YOU WERE GOING", speed, "KM/H ... YOU WERE", difference, "KM/H", overUnder,"* \n THANK YOU FOR USING OUR SERVICE! :)")
else:
    print("\nOKAY, THANK YOU FOR USING THIS SERVICE!")
