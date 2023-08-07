# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format
# You have x days, y weeks, and z months left.
# Where x, y and z are replaced with the actual calculated numbers.
# There are 365 days in a year, 52 weeks in a year and 12 months in a year.

age = int(input("What is your current age? \n"))

daysinYear = 365
weeksinYear = 52
monthsinYear = 12

totalDays = daysinYear * 90
totalWeeks = weeksinYear * 90
totalMonths = monthsinYear * 90

numofDaysLived = age * daysinYear
numOfWeeksLived = age * weeksinYear
numOfMonthsLived = age * monthsinYear

daysLeft = totalDays - numofDaysLived
weeksLeft = totalWeeks - numOfWeeksLived
monthLeft = totalMonths - numOfMonthsLived


print(f"You have " , daysLeft , " days, ", weeksLeft , " weeks, and ", monthLeft , " left.")
