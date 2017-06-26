#-----------------------------------------------------------------------------------
# 1. Using a loop, ask the user to input scores from nine judges. Scores do not have to be whole numbers.
## a. In the loop, you must identify each judge by their number (from 1 to 9) when asking for their score.
## b. You must verify that the score entered by the judge is between 0.0 and 10.0, inclusive.  You must continually ask a judge to enter their score until their input is the correct range.
## c. Keeping a running sum of all the scores entered by the judges, updating it as each new score comes in.
#-----------------------------------------------------------------------------------



judge_list = []
i = 0

while len(judge_list) < 9:
	i += 1
	score = float(input("Enter judge #%d's score: "%i))
	while score < 0.0 or score > 10.0:
		score = float(input("Re-enter judge #%d's score between 0-10: "%i))
	judge_list.append(score)

####print(judge_list)




#-----------------------------------------------------------------------------------
# 2. After the nine scores are entered, subtract the value of the highest and lowest scores.  (Hint: you will need to keep track of this information with variables and logic.)
#-----------------------------------------------------------------------------------

sorted_scores = sorted(judge_list)
sorted_scores = sorted(judge_list, key=float)

####print(sorted_scores)

####print (sum(sorted_scores))

no_min_no_max = sum(sorted_scores) - min(sorted_scores) - max(sorted_scores)

####print (no_min_no_max)


#-----------------------------------------------------------------------------------
# 3. Average the remaining total for 7 judges and output the final score.
#-----------------------------------------------------------------------------------

average_score = no_min_no_max / 7

####print (average_score)

print ("Your final score is {:0.2f}".format(average_score))

