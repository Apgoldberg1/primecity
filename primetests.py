import math
from itertools import permutations

def prime(number):
    #checks if number has only factors of 1 and itself
    factors = []
    factorsum = 0
    for i in range(math.floor(number / 2)):
        if number % (i + 1) == 0:
            factors.append(i + 1)
    for l in range(len(factors)):
        factorsum += factors[l]
    if factorsum == 1:
        return True
    else:
        return False

def primeunder(n):

    # Create a boolean array "prime[0..n]" and initialize
    # all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):

        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    # Print all prime numbers
    list = []
    for p in range(n + 1):
        if prime[p]:
            list.append(p)
    return list

def twin(number):
    # checks if the number is prime and two away from a prime number
    if prime(number):
        if prime(number + 2) or prime(number - 2):
            return True
        else:
            return False
    else:
        return False


def balanced(number):
    #checks if a number is prime and the primes around it are equally spaced on both sides in other words if they form an arithmatic sequence
    if prime(number):
      try:
        nearestprime = (primeunder(number))[-2]
      except IndexError:
        return False
      searchrange = (2 * number) - nearestprime
      fullsearch = primeunder(searchrange)
      if fullsearch[-1] - number == number - nearestprime and fullsearch[
              -2] == number:
          return True
      else:
          return False
    else:
        return False


"""chen prime needs to be done, uses semiprime"""

def circular(number):
  if prime(number):
    if number<10:
      return True
    else:
      for digit in str(number):
        for evenor5 in ['0','2','4','5','6','8']:
          if digit == evenor5:
            return False
    numberchange = number
    for char in range(len(str(number))):
      numberchange = str(numberchange)
      front = str(numberchange)[0]
      numberchange = numberchange[1:]
      numberchange = int(numberchange+front)
      if not prime(numberchange):
        return False
      else:
        return True
  else:
    return False

'''def allorder(number):
  numberchange = number
  for char in range(len(str(number))):
    numberchange = str(numberchange)
    front = str(numberchange)[0]
    numberchange = numberchange[1:]
    numberchange = int(numberchange+front)
    print(numberchange)'''
#to test reordering numbers

def cousin(number):
    # checks if the number is prime and 4 away from a prime number
    if prime(number):
        if prime(number + 4) or prime(number - 4):
            return True
        else:
            return False
    else:
        return False

def cuban(number):
  if (number-1)%6 == 0 and prime(number):
    if (float((-3+(9-12*(1-number))**(1/2))/6)).is_integer() or (float((-3-(9-12*(1-number))**(1/2))/6)).is_integer():
      return True
    elif ((-6 + ((36-12*(4-number)) ** (1/2)))/6).is_integer() or ((-6 - ((36-12*(4-number)) ** (1/2)))/6).is_integer():
      return True
    else:
      return False
  else:
    return False

"""cullen primes are too large all >2^141"""
def upsidedown(number):
  #flips number upside down if possible on a 7 seg display
  strnumber = str(number)
  strlist = []
  for char in strnumber:
    strlist.append(int(char))
  for digit in range(len(strnumber)):
    if strnumber[digit] == '4' or strnumber[digit] == '3' or strnumber[digit] == '9' or strnumber[digit] == '7' or strnumber[digit] == '6':
      return False
    elif strlist[digit] == 5:
      strlist[digit] = 2
    elif strlist[digit] == 2:
      strlist[digit] = 5
  strnumber = ''
  for i in strlist:
    strnumber+=str(i)
  return int(strnumber)

def dihedral(number):
  #checks if a prime is dihedral meaning it as a 7 segment display upside down, flipped, and upside down and flipped are all prime
  reverse = ''
  strnumber = str(number)
  for i in range(len(strnumber)):
    reverse += strnumber[-(i+1)]
  if prime(int(reverse)) and prime(upsidedown(number)) and prime(upsidedown(reverse)) and prime(number):
    return True
  else:
    return False

"""double mersene prime"""
"""einstein prime"""
def emirp(number):
  #if the prime is still prime when reversed
  reverse = ''
  strnumber = str(number)
  for i in range(len(strnumber)):
    reverse += strnumber[-(i+1)]
  if prime(number) and prime(int(reverse)):
    return True
  else:
    return False

def factorial(number):
  #prime thats one more or less than a factorial
  if prime(number):
    increment = 2
    multiplication = 1
    while multiplication < number+1:
      multiplication *= increment
      increment += 1
    if multiplication - 1 == number:
      return True
    elif (multiplication/(increment-1)) + 1 == number:
      return True
    else:
      return False
  else:
    return False

def pdi_function(number, base: int = 10):
    """Perfect digital invariant function."""
    total = 0
    while number > 0:
        total = total + pow(number % base, 2)
        number = number // base
    return total

def is_happy(number: int) -> bool:
    """Determine if the specified number is a happy number."""
    seen_numbers = []
    while number > 1 and number not in seen_numbers:
        seen_numbers.append(number)
        number = pdi_function(number)
    return number == 1

def happy(number):
  # checks that a number is happy and prime
  if prime(number) and is_happy(number):
    return True
  else:
    return False

def lefttruncatable(number):
  #checks that a number is prime and is still prime after removing the first digit repeatedly
  strnumber = str(number)
  for index in range(len(strnumber)):
    if not prime(int(strnumber[index:])):
      return False
  return True

def righttruncatable(number):
    #checks that a number is prime and is still prime after removing the last digit repeatedly
  strnumber = str(number)
  for index in range(len(strnumber)):
    if not prime(int(strnumber[:index+1])):
      return False
  return True


def rightandlefttruncatable(number):
      #checks that a number is prime and is still prime after removing the last and first digit repeatedly
  strnumber = str(number)
  if len(strnumber) % 2 ==0:
    for index in range(((len(strnumber))//2)):
      if not prime(int(strnumber[index:len(strnumber)-index])):
        return False
  else:
    for index in range(((len(strnumber))//2)+1):
      if not prime(int(strnumber[index:len(strnumber)-index])):
        return False
  return True

def lucas(number):
  if prime(number):
    a=2
    b=1
    while a < number and b < number:
      a = a+b
      b = a+b
    if a == number or b == number:
      return True
    else:
      return False
  else:
    return False

def lucky(number):
  if prime(number):
    luckys = []
    for i in range(1,number+1,2):
      luckys.append(i)
    newentry = 1
    cancelor = luckys[newentry]
    while cancelor < number//2:
      for i in range(cancelor-1,number+1,cancelor):
        try:
          luckys[i] = 'x'
        except IndexError:
          break
      for i in range(len(luckys)):
        try:
          luckys.remove('x')
        except ValueError:
          break
      newentry += 1
      cancelor = luckys[newentry]
    if luckys[-1] == number:
      return True
    else:
      return False
  else:
    return False

def mersene(number):
  if prime(number):
    n = number +1
    return (n != 0) and (n & (n-1) == 0)
  else:
    return False

def doublemersene(number):
  if prime(number):
    n = number +1
    if (n != 0) and (n & (n-1) == 0):
      return math.log(math.log(n, 2)+1,2).is_integer()
  else:
    return False

def palindromic(number):
  if prime(number):
    reverse = ''
    number = str(number)
    for i in range(len(number)):
      reverse += number[-(i+1)]
    if reverse == number:
      return True
    else:
      return False
  else:
    return False

def absolute(number):
  #any permutations results in a prime
  lstnum = []
  for i in str(number):
    lstnum.append(i)
  perm = permutations(lstnum)
  for num in list(perm):
    test = ''
    for digit in num:
      test += digit
    if not prime(int(test)):
      return False
  return True

def factor(n):
  #returns prime factorization in a list
      i = 2
      factors = []
      while i * i <= n:
          if n % i:
              i += 1
          else:
              n //= i
              factors.append(i)
      if n > 1:
          factors.append(n)
      return factors

def pierpont1(number):
  if prime(number):
    primelist = factor(number-1)
    for i in primelist:
      if i != 2 and i !=3:
        return False
    return True
  else:
    return False

def pierpont2(number):
  if prime(number):
    primelist = factor(number+1)
    for i in primelist:
      if i != 2 and i !=3:
        return False
    return True
  else:
    return False

def sexy(number):
    # checks if the number is prime and 4 away from a prime number
    if prime(number):
        if prime(number + 6) or prime(number - 6):
            return True
        else:
            return False
    else:
        return False

def quadruplet(number):
  if prime(number) and prime(number+2):
    if prime(number+6) and prime(number+8) or prime(number-4) and prime(number-6):
      return True
    else:
      return False
  elif prime(number) and prime(number-2):
    if prime(number-6) and prime(number-8) or prime(number+4) and prime(number+6):
      return True
  else:
    return False

def triplet(number):
  if prime(number) and (prime(number+2) or prime(number+4)) and prime(number+6):
    return True
  number -=2
  if prime(number) and (prime(number+2) or prime(number+4)) and prime(number+6):
    return True
  number-= 2
  if prime(number) and (prime(number+2) or prime(number+4)) and prime(number+6):
    return True
  number-=2
  if prime(number) and (prime(number+2) or prime(number+4)) and prime(number+6):
    return True
  return False

def primorial(number):
  if not prime(number):
    return False
  primes = open("primelist.txt")
  primelist = primes.read()
  primelist = primelist.split(",")
  primorial = 1
  count = 0
  while primorial <= number:
    primorial *= int(primelist[count])
    count+=1
  if primorial - 1 == number or primorial/int(primelist[count-1]) + 1 == number:
    return True
  return False

def pythagorean(number):
  if not prime(number):
    return False
  if (number-1)%4 == 0:
    return True
  else:
    return False

def sophiegermain(number):
  if prime(number) and prime(2*number + 1):
    return True
  else:
    return False

def safe(number):
  if prime(number) and prime((number-1)/2):
    return True
  else:
    return False

def strobogrammatic(number):
  def reverse(number):
    reverse = ''
    strnumber = str(number)
    for i in range(len(strnumber)):
      reverse += strnumber[-(i+1)]
    return reverse
  if not prime(number):
    return False
  strnumber = str(number)
  for i in range(len(strnumber)):
    if strnumber[i] == '2' or strnumber[i] == '3' or strnumber[i] == '4' or strnumber[i] == '5' or strnumber[i] == '7':
      return False
    if strnumber[i] == '9':
      strnumber = strnumber.replace(strnumber[i], 'x')
    if strnumber[i] == '6':
      strnumber = strnumber.replace(strnumber[i], 'y')
  for i in range(len(strnumber)):
    try:
      strnumber = strnumber.replace('y', '9')
    except ValueError:
      break
    try:
      strnumber = strnumber.replace('x', '6')
    except ValueError:
      break
  if int(reverse(strnumber)) == number:
    return True
  else:
    return False

def strong(number):
  if not prime(number):
    return False
  if number == 2:
    return False
  primes = open("primelist.txt")
  primelist = primes.read()
  primelist = primelist.split(",")
  index = primelist.index(' ' + str(number))
  if (int(primelist[index-1]) + int(primelist[index+1]))/2 < number:
    return True
  return False

def weak(number):
  if not prime(number):
    return False
  if number == 2:
    return False
  primes = open("primelist.txt")
  primelist = primes.read()
  primelist = primelist.split(",")
  index = primelist.index(' ' + str(number))
  if (int(primelist[index-1]) + int(primelist[index+1]))/2 > number:
    return True
  return False
  
def superprime(number):
  if not prime(number):
    return False
  primes = open("primelist.txt")
  primelist = primes.read()
  primelist = primelist.split(",")
  if prime(primelist.index(' ' + str(number))+1):
    return True
  return False

def wagstaff(number):
  if not prime(number):
    return False
  if prime(math.log((3*number)-1, 2)):
    return True
  return False
