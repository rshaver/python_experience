


    
import math

####1. Ask the user to input the target's distance in meters, which will be a positive floating point number.

targetDistance = -1


while targetDistance < 0:
  try:
      targetDistance = float(input("Enter target distance in Meters: "))
  except ValueError:
      print("Please enter an integer zero or greater")












differenceTD = 10

while differenceTD > 1 or differenceTD < 0:




  ####2. Ask the user to input the amount of kilograms of gun powder they would like to use in the cannon, which will be a positive foating point number.

  gunPowder = -1

  while gunPowder < 0:
    try:
      gunPowder = float(input("Enter Kiolograms of gunpowder to load: "))
    except ValueError:
      print("Please enter an integer zero or greater")


  ####3. Ask the user to input the angle in degrees that they would like to fire the cannon at, which will be a positive floating point number no larger than 90degrees.

  angleDegrees = -1


  

  while angleDegrees < 0 or angleDegrees > 90:
    try:
      angleDegrees = float(input("Please enter firing angle between 0-90 degrees: "))
    except ValueError:
      print("Please enter an integer between 0 and 90")



  ####4. Using several statements, calculate how far the cannonball will travel before hitting the ground.

  velocity = gunPowder * 10
  theta = angleDegrees 


  thetaRadians = theta * (math.pi / 180) 


  Vy = math.sin(thetaRadians) * velocity
  Vx = math.cos(thetaRadians) * velocity

  Ta = Vy / 9.8
  Tg = Ta * 2

  distanceTraveled = Tg * Vx 







  ####5. Determine if the cannonball landed within 1.0m of the target. Use 9.8 as the acceleration due to gravity.


  differenceTD = distanceTraveled - targetDistance
  
  if differenceTD > 1 or differenceTD < 0:
    print ("You missed the mark by {:0.2f}".format(differenceTD) + " meters.  Try again.")



print ("You hit the target!")