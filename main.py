import math
import operator as op
from functools import reduce

# Change the rounding digit when desired so you don't have to think
round_digit = 4

# Does the poisson calculations
def poisson(mean, x):
  result = ((mean ** x) * math.exp((-mean))) / (math.factorial(x))
  return(result)

# Does the nCr function
def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom

# Description of each probability in case I forget
print("Geometric (1): Probability of the first success (first shot in the basket)")
print("Poisson (2): Given mean, calculates the probability of success over a interval (hurricanes/year)")
print("Binomial (3): Probability of given number of success in a given number of trials (out of 5 people, how many are weirdos)\n")
    
while True:
  distributionType = int(input("Type: "))
  # Geometric
  if distributionType == 1:
    method = int(input("""One-time calculation (1)\nMultiple calculations - range (2): """))
    

    if method == 1:
      x = int(input("Number of the trials needed for success: "))

      # p needs to be decimal
      p = float(input("Probability of success: "))
      q = 1 - p

      result = p * (q**(x-1))
      print("RESULT: " + str(round(result, round_digit)))
      print()

    elif method == 2:
      counter = int(input("Number of calculations: "))
      p = float(input("Probability of success: "))
      q = 1 - p
      result = 0
      for number in range(counter):
        x = int(input("Number of the trials needed for success: ")) 
        result += p * (q**(x-1))
      print("RESULT: " + str(round(result, round_digit)))
      print()

  # Poisson
  elif distributionType == 2:
    method = int(input("""One-time calculation (1)\nMultiple calculations - range (2): """))

    if method == 1:
      mean = float(input("Mean: "))
      x = float(input("Number of successes: "))
      result = 0
      print("RESULT: " + str(round(poisson(mean, x), round_digit)))
      print()

    elif method == 2:
      counter = int(input("Number of calculations: "))
      mean = float(input("Mean: "))
      result = 0
      for number in range(counter):
        x = float(input("Number of successes: "))
        result += poisson(mean, x)
      print("RESULT: " + str(round(result, round_digit)))
      print()

  # Binomial
  elif distributionType == 3:
    method = int(input("""One-time calculation (1)\nSum of a range of x (2)\nAll results of a range of x separately (3): """))
    if method == 1:
      n1 = int(input("Number of trials: "))
      x = int(input("Successful trials: "))
      p = float(input("Successful rate: "))
      q = 1 - p

      print("RESULT: " + str(round(ncr(n1, x)*(p**x)*(q**(n1-x)), round_digit)))
      print()

    elif method == 2:
      counter = int(input("How many calculations?: "))
      n1 = int(input("Number of trials: "))
      p = float(input("Successful rate: "))
      q = 1 - p
      result = 0
      for number in range(counter):
        x = int(input("Successful trials: "))
        result += ncr(n1, x)*(p**x)*(q**(n1-x))
      print("RESULT: " + str(round(result, round_digit)))
      print()
      
    # Shortcut to make multiple one-time calculations. Just because the homework likes to ask for a bunch of stuff
    elif method == 3:
      counter = int(input("How many calculations?: "))
      n1 = int(input("Number of trials: "))
      p = float(input("Successful rate: "))
      q = 1 - p
      for number in range(counter):
        x = int(input("Successful trials: "))
        print("RESULT: " + str(round(ncr(n1, x)*(p**x)*(q**(n1-x)), round_digit)))
      print()