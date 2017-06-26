####--------------------------- FUNCTION AREA ---------------------------

#A function get_prime_limit, which takes no parameters.
#It asks the user to input the upper limit value N, 
#validates that it is greater than 2, and returns it.
def get_prime_limit():

  N = int(input("How long should we search for primes? Until N =: "))
  while N < 2:
    N = int(input("How long should we search for primes? Until N =: "))
  return N





#A function make_sieve, which is passed a parameter for N (From the previous step).  
#It creates the list of size N-1, 
#and computes the True or False values for each entry in the list using the Sieve of Erathosthenes.
#The computed list is returned.
def make_sieve(N):
  sieve = [True] * (N - 1)
  num = 2
  while num < N:
    if sieve[num - 2] == True:
      #update every multiple of num, set sieve to false for that number
      multiple = num * 2
      while multiple < N:
        sieve[multiple - 2] = False
        multiple = multiple + num
      #go to next multiple
    num += 1
  return sieve






#A function get_check, which takes no parameters.  
#It asks the user to input an integer to check for prime-ness, 
#validates that it is greater than 1, and returns it.
def get_check(N):
  x = 0
  while x <= 1 or x >= N:
    x = int(input("What number should we test for primeness? 0 to quit:  "))
    if x == 0:
      quit()
  return x





#A function is_prime, which takes the Sieve list returned from make_sieve, 
#and the integer read from get_check, 
#and examines the given Sieve list to see if the given number is prime.  
#It returns True if the number is prime, and False if it is not.  
def is_prime(sieve_list, integer):
  if sieve_list[integer - 2] == True:
    return True
  else:
    return False
  



  
#A function is_mersenne_prime, which takes a number assumed to be prime as a parameter.  
#It returns True if that number is also a Mersenne prime.  
#It does not need to double-check to make sure the number is prime.  
def is_mersenne_prime(prime):
  n = 0
  x = 0
  while x <= prime:
      x = 2 ** n - 1
      if(prime == x):
          return True
      n += 1
      
  return False


 
  
  
####--------------------------- MAIN() AREA ---------------------------  
def main():

  N = get_prime_limit()
  sieve_list = make_sieve(N)
  
  num_to_check = 1

  while num_to_check != 0:
    num_to_check = get_check(N)
  

    prime = num_to_check
    
    if is_prime(sieve_list, num_to_check) == True:
      print("{0} is prime!".format(num_to_check))
      
      if (is_mersenne_prime(prime)) == True:
        print ("{0} is a Mersenne Prime as well!".format(prime) + " It is equal to 2^n - 1")
      else:
        print()
          
    else:
      print ("{0} isn't prime :(".format(num_to_check))


    
main()



