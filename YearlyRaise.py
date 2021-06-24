#-----------------------------------------------------------------------
# Neina Cichon
# Yearly Raise (While Loop Style)
# Date: June 13, 2020
#-----------------------------------------------------------------------
# Declaring Variables
dblHourlyRate = float(input("Please enter your current hourly rate: ")) # Question one, asks user for rate input and puts it into a variable
dblRaisePercentage= float(input("Please enter your expected yearly raise percentage(Whole Number): ")) #Question 2 asks user for raise input and puts it into a variable
dblRaisePercentage = dblRaisePercentage / 100 #Change Whole Number Percent to decimal
intYearlyHours = 2080 # Number of hours in a year assigned to yearly hours (40 hrs /wk for 52 weeks)
dblSalary = (dblHourlyRate * intYearlyHours) # multiplying Rate by hours to get initial salary
intYear = 1 # Assigning 1 to year variable to use as year # and counter

#loop to get salary increase results for 10 years
while intYear < 11:
    if intYear == 1:
        print("Year ", intYear, " -- $", format(dblSalary, ','))
        intYear += 1
        pass
    else:
        dblSalary= dblSalary + (dblSalary * dblRaisePercentage)
        print("Year ", intYear, " -- $", format(dblSalary, ','))
        intYear += 1

