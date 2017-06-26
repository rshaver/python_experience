# 1. Ask the user to input the player's full name

playerName = str(input("Input player's full name: "))


# 2. Ask the user eto enter these values, and save them to variables: 
# (a) At Bats
# (b) Singles
# (c) Doubles
# (d) Triples
# (e) Home Runs


singles = float(input("Enter Singles Values: "))

doubles = float(input("Enter Doubles Values: "))

triples = float(input("Enter Triples Values: "))

homeRuns = float(input("Enter Home Run Values: "))

totalHits = (singles + doubles + triples + homeRuns)


#atBats must be greater than or equal to totalHits
atBats = float(input("Enter At Bat Values: "))


while (atBats < totalHits):
    atBats = float(input("Please enter At Bat value greater than or equal to Total Hits: "))




#3.
print "Did you know that " + str(playerName) + "'s total hits was " + str(totalHits) + "?"




#4. 
battingAverage = totalHits / atBats
battingAverage = str(round(battingAverage,3))
print "Did you also know that " + str(playerName) + "'s batting average was " + str(battingAverage) + "?"



#5.
sluggingPercentage = ((singles * 1) + (doubles * 2) + (triples * 3) + (homeRuns * 4)) / atBats
sluggingPercentage = str(round(sluggingPercentage,3))
print "In addition, did you know that " + str(playerName) + "'s slugging percentage was " + str(sluggingPercentage) + "?"






