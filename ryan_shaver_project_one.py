#### -----------------------0. MENU  ----------------------

choice = 1
while ((choice == 1) or (choice == 2) or (choice == 3) or (choice == 4)):
  print ()
  print ("-------------------------------")
  print ("Main Menu:")
  print ("1. Travel Time")
  print ("2. Cost of Gas")
  print ("3. Used Value")
  print ("4. Stopping Distance")
  print ("-------------------------------")
  print()
  
  choice = int(input("Choose a function: "))
  
  
  while (choice > 4) or (choice <=0):
    choice = int(input("Please input integer between 1-4: "))
  
  
  
#### ----------------------1. TRAVEL TIME  ----------------------

  if choice == 1:
    
    distanceEnter_1 = float(input("Enter distance (miles): "))
    while distanceEnter_1 <= 0.0:
      distanceEnter_1 = (float(input("Please input integer greater than zero: ")))
    
    speedEnter_1 = float(input("Enter speed (miles per hour): "))
    while speedEnter_1 <= 0.0:
      speedEnter_1 = (float(input("Please input integer greater than zero: ")))

    minutes_1 = 60      
    
    print()
    print ("It takes " + str((distanceEnter_1 / speedEnter_1) * minutes_1) + " minutes to travel " + str(distanceEnter_1) + " miles at " + str(speedEnter_1) + " miles per hour.")
    
 
 
 #### ----------------------2. COST OF GAS  ---------------------- 
    
  if choice == 2:
    
    carOne_mpg_2 = float(input("Enter car 1's MPG: "))
    while carOne_mpg_2 <= 0.0:
      carOne_mpg_2 = (float(input("Please input integer greater than zero: ")))
    carOne_gasCost_2 = float(input("Enter car 1's average gas cost per gallon: "))
    while carOne_gasCost_2 <= 0.0:
      carOne_gasCost_2 = (float(input("Please input integer greater than zero: ")))
    
    
    carTwo_mpg_2 = float(input("Enter car 2's MPG: "))
    while carTwo_mpg_2 <= 0.0:
      carTwo_mpg_2 = (float(input("Please input integer greater than zero: ")))
    carTwo_gasCost_2 = float(input("Enter car 2's average gas cost per gallon: "))
    while carTwo_gasCost_2 <= 0.0:
      carTwo_gasCost_2 = (float(input("Please input integer greater than zero: ")))
    
    
    milesDriven_2 = float(input("Miles driven per month: "))
    while milesDriven_2 <= 0.0:
      milesDriven_2 = (float(input("Please input integer greater than zero: ")))    
    
    #calculuating annaul cost by giving months of the year... which is 12
    months_2 = 12
    carOne_yearCost_2 = ((milesDriven_2 / carOne_mpg_2) * (carOne_gasCost_2)) * months_2
    carTwo_yearCost_2 = ((milesDriven_2 / carTwo_mpg_2) * (carTwo_gasCost_2)) * months_2
    
    if carOne_yearCost_2 > carTwo_yearCost_2:
      print()
      print ("Car 2 will save ${:0.2f}".format(carOne_yearCost_2 - carTwo_yearCost_2) + " in a year.")
    
    elif carOne_yearCost_2 == carTwo_yearCost_2:
      print()
      print ("The two cars cost the same.")
    
    else:
      print ()
      print ("Car 1 will save ${:0.2f}".format(carTwo_yearCost_2 - carOne_yearCost_2) + " in a year.")
      print ()
    
    
      
    


#### ----------------------3. USED VALUE ----------------------
  
  if choice == 3:
  
    orignalPrice = float(input("Enter orignal price of car: "))
    while orignalPrice <= 0.0:
      orignalPrice = (float(input("Re-enter orignal price of car: ")))    
    
    years_input = int(input("Enter number of years: "))
    while years_input <= 0.0:
      years_input = (int(input("Re-enter number of years: ")))    
    
    depreciation = .18
    i = 0
    
    #this while loop takes the originalPrice then depreciates said orignalPrice, then uses it as the new value of the car, which then iterates as many times as the user inputed which results in a subsequent depreciation each year.
    while i < years_input:
    	i += 1
    	new_value = orignalPrice - (orignalPrice * depreciation)
    	orignalPrice = new_value
    	print ("Year %d value: {:0.2f}".format(new_value)%i)




#### ----------------------4. STOPPING DISTANCE ----------------------

  if choice == 4:
    initialSpeed = float(input("Enter initial speed: "))
    while initialSpeed <= 0.0:
      initialSpeed = float(input("Re-enter initial speed: "))
    tireCondition = float(input("Enter tire condition (1 = new, 2 = good, 3 = poor): "))
    while tireCondition <= 0 or tireCondition > 3:
      tireCondition = float(input("Re-enter tire condition (1 = new, 2 = good, 3 = poor): "))

    if tireCondition == 1:
      tireCondition = .8
      tireName = str("new")
    elif tireCondition == 2:
      tireCondition = .6
      tireName = str("good")
    elif tireCondition == 3:
      tireCondition = .5
      tireName = str("bad")

    #converted 9.8 meters squared to feet
    #converted 1 mph to 1.46667 feet per second
    gravity = 32.174
    initialSpeedConverted = initialSpeed * 1.46667

    numerator = (initialSpeedConverted) * (initialSpeedConverted)
    denominator = 2 * tireCondition * gravity

    distance = numerator / denominator

    print()
    print ("At {:0.0f} miles per hour, with ".format(initialSpeed) + str(tireName) + " tires, the car will stop in {:0.2f}".format(distance) + " feet.")

