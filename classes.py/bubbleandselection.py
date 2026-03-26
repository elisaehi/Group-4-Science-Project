'''
seatingChart = [["A", True, "B", True], ["C", False, "D", True], ["E", False,"F", True]]
present = 0

for row in seatingChart:
    for i in row:
        if i == True:
            present += 1
        elif i == False:
            print(seatingChart[i-3])
'''

class Rainfall:
    def __init__(self):

        # 2D list storing rainfall data
        self.rain = [[5.2, 0.0, 3.1, 10.4, 2.5, 0.0, 1.8],[0.0, 4.3, 6.7, 2.1, 0.0, 0.0, 3.9],[7.2, 8.1, 0.0, 1.4, 2.0, 5.6, 0.0],[0.0, 3.3, 2.9, 0.0, 4.8, 6.1, 2.7]]
        self.days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

    # Method to calculate average rainfall
    def average_rainfall(self):
      # write your code here
      for i in self.rain





    # Method to find highest rainfall day

    def highest_rainfall_day(self):



        max_rain = -1

        day_name = ""

       # write your code here

        return day_name, max_rain





# Creating object

r = Rainfall()



# Average rainfall

print("Average rainfall for the month:", r.average_rainfall(), "mm")



# Highest rainfall day

day, value = r.highest_rainfall_day()

print("Highest rainfall occurred on:", day)

print("Rainfall amount:", value, "mm")

            